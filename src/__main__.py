from uvicorn import run

from bio_stats_service.create_app import create_app

app = create_app()
run(app, host="0.0.0.0")
