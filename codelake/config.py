import os
import logging
import argparse
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("codelake.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def main():
    # Load environment variables from .env file
    load_dotenv()
    
    # Configure command line arguments
    parser = argparse.ArgumentParser(description='codelake: Deep Lake-powered code generation')
    parser.add_argument('--ingest', action='store_true', help='Ingest SDK documentation')
    parser.add_argument('--interactive', action='store_true', help='Run in interactive mode')
    parser.add_argument('--api', action='store_true', help='Start API server')
    parser.add_argument('--sdk-repo', type=str, help='GitHub repository URL of the SDK')
    parser.add_argument('--dataset-path', type=str, default=os.environ.get('DEEPLAKE_DATASET_PATH'), 
                        help='Deep Lake dataset path')
    args = parser.parse_args()
    
    # Confirm API keys are available
    required_keys = ['OPENAI_API_KEY', 'ACTIVELOOP_TOKEN']
    for key in required_keys:
        if not os.environ.get(key):
            logger.error(f"Missing environment variable: {key}")
            return

    # Import service functions here to avoid circular imports
    from codelake.service import run_service, run_interactive_session
    from codelake.ingest.documentation_ingest import ingest_sdk_documentation
    
    # Process command
    if args.ingest:
        if not args.sdk_repo:
            logger.error("SDK repository URL required for ingestion")
            return
        ingest_sdk_documentation(args.sdk_repo, args.dataset_path)
    elif args.interactive:
        run_interactive_session(args.dataset_path)
    elif args.api:
        run_service(args.dataset_path)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
