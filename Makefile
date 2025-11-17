# This line will read the .env file (if it exists) and load the variables
-include .env

# Set the default port if it wasn't in the .env file
# The ?= operator means "set if not already set"
HTTP_PORT ?= 8880 
HTTPS_PORT ?= 8443

# This is the main target. Running "make" or "make up" will run this.
up:
	@echo "Starting CTI Assessment Tool in the background..."
	@docker-compose up -d
	@echo ""
	@echo "=========================================================="
	@echo "✅  Success! Your CTI Assessment Tool is now running."
	@echo ""
	@echo "  Please visit: https://localhost:$(HTTPS_PORT)"
	@echo ""
	@echo "  NOTE: Your browser will show a 'privacy warning'."
	@echo "  This is expected. Please click 'Advanced' and 'Proceed'."
	@echo "=========================================================="

# This target will be run when the user types "make down"
down:
	@echo "Stopping CTI Assessment Tool..."
	@docker-compose down
	@echo "Done."

# This makes "up" the default command if the user just types "make"
.DEFAULT_GOAL := up
