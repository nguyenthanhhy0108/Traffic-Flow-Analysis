# Run backend
echo "Starting Flask backend..."
python backend.py&

# Run frontend
echo "Starting Streamlit frontend..."
streamlit run Streamlit.py --server.port 8070

# Cleanup
echo "Stopping Flask backend..."
pkill -f "python backend.py"