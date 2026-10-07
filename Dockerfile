FROM python:3.11-slim

WORKDIR /app

COPY requirements /app/requirements

RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir --default-timeout=300 -r requirements/streamlit.txt

COPY . .

EXPOSE 8501

CMD ["sh", "-c", "streamlit run app/app.py --server.address=0.0.0.0 --server.port=$PORT"]