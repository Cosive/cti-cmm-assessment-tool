# CTI-CMM Web Assessment Tool

[](https://opensource.org/licenses/MIT)

This is a stand-alone web application to help you self-evaluate your current maturity against the [CTI-CMM's](https://cti-cmm.org/) 11 domains. It provides an interactive, browser-based alternative to the spreadsheet version of the CTI-CMM, with all data saved locally to your machine.

This tool runs entirely in your browser and is served by a secure, local-only web server. **No assessment data ever leaves your computer.**

## Features

  * **Interactive Assessment:** Interactively score 11 CTI-CMM domains and assessment practices.
  * **Visual Dashboard:** A dashboard page visualizes your overall maturity and domain-by-domain completion.
  * **Planning Mode:** Toggle between "Benchmark Mode" (for `Current` scores) and "Planning Mode" (for `Target` scores, `Impact`, `Effort`, and `Priority`).
  * **Priorities Planning:** A "Priorities Sheet" aggregates all practices where `Target > Current` to help you sort, filter, and plan your improvement journey.
  * **Auto-Saving:** All scores, notes, and planning data are saved automatically to your browser's local storage.
  * **Data Management:** Export and Import your complete assessment as a single `.json` file for backup or sharing.
  * **Locally hostable:** Runs 100% locally via Docker (or just use `python -m http.server` if preferred)).

## How to Run the Tool

This application is containerized and designed to be run with a single command.

### Prerequisites

  * **Docker**
  * **Docker Compose**
  * **`make`** (This is used for a simpler start/stop experience. It is pre-installed on most macOS and Linux systems. Windows users can use `make` via WSL.)

### 1\. Clone the Repository
First, clone this repository to your local machine:

```bash
git clone https://github.com/chorsley/cti-cmm-assessment-tool.git
cd cti-cmm-assessment
```

### 2\. Start the Application

After cloning the repository, navigate into the directory and run:

```bash
make up
```

This command will:

1.  Build and run the application in the background using `docker-compose`.
2.  Start a HTTPS-capable Caddy web server that serves the tool.
3.  Automatically create a self-signed certificate for `https://localhost:8443`.
4.  Print a success message with the correct URL to visit.

You will see output similar to this:

```
Starting CTI Assessment Tool in the background...

==========================================================
✅  Success! Your CTI Assessment Tool is now running.

  Please visit: https://localhost:8443

  NOTE: Your browser will show a 'privacy warning'.
  This is expected. Please click 'Advanced' and 'Proceed'.
==========================================================
```

### 3\. Access the Tool in Your Browser

Open your browser and go to: **`https://localhost:8443`**

#### ⚠️ Browser Privacy Warning

Your browser will show a **"Your connection is not private"** warning since we are self-hosting.

**To proceed, simply click "Advanced" and then "Proceed to localhost (unsafe)".**

### 4\. Stop the Application

When you are finished, you can stop the container by running:

```bash
make down
```

This will stop and remove the Docker container, but your assessment data will remain safe in your browser's local storage or your JSON export file (if you saved one).

### Troubleshooting: Port Conflicts

If you see an error like `port is already allocated`, it means another service on your machine is already using port `80` or `443`.

**To fix this:**

1.  Create a new file in this directory named `.env`

2.  Add your desired ports to this file. For example:

    ```
    # .env file
    HTTPS_PORT=8443
    HTTP_PORT=8080
    ```

3.  Run `make up` again. The success message will now show your new URL:

    `Please visit: https://localhost:8443`

### Data Persistence and Backup

  * **Browser Storage:** All your data is saved in your browser's Local Storage. You can safely stop the container (`make down`) and start it again (`make up`);your data will still be there.
  * **Backups:** To back up your work or move it to another computer, go to the **Data Management** page and use the **"Export Results (.json)"** button. You can use the "Import Results" button on another machine to restore your progress.
  * **Multiple assessments:** You can maintain multiple assessments by exporting different JSON files and importing them as needed. To differentiate assessments, can name your current assessment in the Data Management page which will be saved in the JSON file.
  * **Sharing:** You can share your assessment JSON export file with colleagues for collaborative review.

## Author & License

This tool is maintained by **Chris Horsley** at [Cosive](https://cosive.com). PRs and issues very welcome!

This project is licensed under the **MIT License**.