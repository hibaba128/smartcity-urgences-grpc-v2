from fastapi import FastAPI
import grpc
import urgence_pb2, urgence_pb2_grpc

app = FastAPI()

channel = grpc.insecure_channel('localhost:50051')
stub = urgence_pb2_grpc.UrgenceServiceStub(channel)

@app.post("/alert")
def create_alert(alert: dict):
    req = urgence_pb2.AlertRequest(**alert)
    resp = stub.CreateAlert(req)
    return {"alertId": resp.alertId, "message": resp.message}

@app.get("/status/{alert_id}")
def get_status(alert_id: str):
    req = urgence_pb2.StatusRequest(alertId=alert_id)
    resp = stub.GetAlertStatus(req)
    return {"status": resp.status}
