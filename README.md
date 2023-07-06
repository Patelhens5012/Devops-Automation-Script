# Devops-Automation-Script
This script demonstrates several challenging aspects of DevOps automation:

Git operations: The script uses the subprocess module to execute Git commands, such as cloning a repository. It assumes that Git is installed and properly configured.

Build and test automation: The script executes build and test commands using the subprocess module. It assumes that the project has a Makefile or an equivalent build system in place.

Deployment: The script copies the packaged application to the web server's directory and restarts the web server using subprocess calls. It assumes the existence of a web server (e.g., Apache) and proper permissions for deployment.

Error handling and cleanup: The script performs error handling by checking for the existence of the deployed application and cleaning up temporary files and directories after the deployment is complete.

