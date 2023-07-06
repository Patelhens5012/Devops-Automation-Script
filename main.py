import subprocess
import shutil
import os

def deploy_application():
    # Clone the application repository
    subprocess.run(["git", "clone", "https://github.com/example/application.git"])

    # Build the application
    subprocess.run(["make", "build"], cwd="application")

    # Run unit tests
    subprocess.run(["make", "test"], cwd="application")

    # Package the application
    subprocess.run(["make", "package"], cwd="application")

    # Deploy the application
    shutil.copy("application/package.tar.gz", "/var/www")

    # Restart the web server
    subprocess.run(["systemctl", "restart", "apache2"])

    # Clean up
    shutil.rmtree("application")

def main():
    # Check if the application is already deployed
    if os.path.exists("/var/www/package.tar.gz"):
        print("Application already deployed. Skipping deployment.")
        return

    # Perform the deployment
    deploy_application()

if __name__ == "__main__":
    main()
