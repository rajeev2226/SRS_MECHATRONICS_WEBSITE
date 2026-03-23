from flask import Flask, render_template
import logging
import os

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Log static folder path
static_path = os.path.join(app.root_path, 'static')
logger.info(f"Static folder path: {static_path}")
logger.info(f"Static folder exists: {os.path.exists(static_path)}")

if os.path.exists(static_path):
    static_files = os.listdir(static_path)
    logger.info(f"Static files: {static_files}")

@app.route('/')
def home():
    logger.info("Serving home page")
    try:
        return render_template('home.html')
    except Exception as e:
        logger.error(f"Error rendering home template: {e}")
        return f"Error: {e}", 500

@app.route('/about')
def about():
    logger.info("Serving about page")
    try:
        return render_template('about.html')
    except Exception as e:
        logger.error(f"Error rendering about template: {e}")
        return f"Error: {e}", 500

@app.route('/products/chemical')
def chemical():
    logger.info("Serving chemical products page")
    try:
        return render_template('chemical.html')
    except Exception as e:
        logger.error(f"Error rendering chemical template: {e}")
        return f"Error: {e}", 500

@app.route('/products/electrical')
def electrical():
    logger.info("Serving electrical products page")
    try:
        return render_template('electrical.html')
    except Exception as e:
        logger.error(f"Error rendering electrical template: {e}")
        return f"Error: {e}", 500

@app.route('/products/environmental')
def environmental():
    logger.info("Serving environmental products page")
    try:
        return render_template('environmental.html')
    except Exception as e:
        logger.error(f"Error rendering environmental template: {e}")
        return f"Error: {e}", 500

@app.route('/products/fire-smoke')
def fire_smoke():
    logger.info("Serving fire-smoke products page")
    try:
        return render_template('fire-smoke.html')
    except Exception as e:
        logger.error(f"Error rendering fire-smoke template: {e}")
        return f"Error: {e}", 500

@app.route('/products/optical')
def optical():
    logger.info("Serving optical products page")
    try:
        return render_template('optical.html')
    except Exception as e:
        logger.error(f"Error rendering optical template: {e}")
        return f"Error: {e}", 500

@app.route('/products/sample-prep')
def sample_prep():
    logger.info("Serving sample-prep products page")
    try:
        return render_template('sample-prep.html')
    except Exception as e:
        logger.error(f"Error rendering sample-prep template: {e}")
        return f"Error: {e}", 500

@app.route('/services')
def services():
    logger.info("Serving services page")
    try:
        return render_template('services.html')
    except Exception as e:
        logger.error(f"Error rendering services template: {e}")
        return f"Error: {e}", 500

@app.route('/contact')
def contact():
    logger.info("Serving contact page")
    try:
        return render_template('contact.html')
    except Exception as e:
        logger.error(f"Error rendering contact template: {e}")
        return f"Error: {e}", 500

if __name__ == '__main__':
    print("\n===============================================")
    print("Flask server starting with enhanced logging...")
    print("Static folder:", static_path)
    print("Static files:", os.listdir(static_path) if os.path.exists(static_path) else "None")
    print("Please open your browser to: http://localhost:5000")
    print("Press Ctrl+C to stop the server.")
    print("===============================================\n")

    # Enable detailed logging
    app.logger.setLevel(logging.DEBUG)

    app.run(debug=True, host='0.0.0.0', port=5000)