import os
import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

app = FastAPI(
    title="Project Axiom Guide: Cloud Simulation Engine",
    version="3.0.0"
)

HISTORICAL_SANDBOX = {
    "roman_republic_79ad": {
        "name": "The Roman Republic Collapse (79 AD)",
        "mortality_load_change": 0.15,
        "resource_depletion_rate": 1.1,
        "dunbar_trust_index": 0.25,
        "cognitive_autonomy_ratio": 0.30
    },
    "singapore_1965": {
        "name": "Singapore Transition Framework (1965)",
        "mortality_load_change": -0.45,
        "resource_depletion_rate": 0.85,
        "dunbar_trust_index": 0.88,
        "cognitive_autonomy_ratio": 0.85
    },
    "easter_island_1600": {
        "name": "Easter Island Ecological Burn (1600 AD)",
        "mortality_load_change": 0.70,
        "resource_depletion_rate": 3.5,
        "dunbar_trust_index": 0.10,
        "cognitive_autonomy_ratio": 0.15
    },
    "weimar_germany_1923": {
        "name": "Weimar Germany Hyperinflation (1923)",
        "mortality_load_change": 0.05,
        "resource_depletion_rate": 1.0,
        "dunbar_trust_index": 0.35,
        "cognitive_autonomy_ratio": 0.40
    }
}

class TelemetryPayload(BaseModel):
    dunbar_trust_index: float
    cognitive_autonomy_ratio: float
    resource_depletion_rate: float
    mortality_load_change: float

def run_calculation(dunbar_trust, cognitive_autonomy, resource_depletion, mortality_change):
    utility = (dunbar_trust + cognitive_autonomy) / 2
    drain = resource_depletion * (1 + mortality_change)
    if drain <= 0: return 0.0
    return round(utility / drain, 4)

def get_status_matrix(efficiency):
    if efficiency < 0.5:
        return "🟥 CRITICAL SYSTEM FAILURE: PARASITIC CODE", "Trigger Algorithmic Quarantine & Economic Shunning (Chapter 11/12 Firewall).", "#ef4444"
    elif 0.5 <= efficiency < 1.0:
        return "🟨 SYSTEM STAGNATION: BRITTLE CODE", "Deploy Micro-Niche Allocation Adjustments to optimize systemic load metrics.", "#eab308"
    else:
        return "🟩 OPTIMIZED OPERATION: SYMBIOTIC COOPERATIVE", "Approve code variant; export structural design patterns to open registry.", "#22c55e"

@app.get("/")
def read_root():
    # Safely serves the decoupled HTML interface file from disk
    return FileResponse("index.html")

@app.get("/audit/{event_id}")
def audit_historical_event(event_id: str):
    event = HISTORICAL_SANDBOX.get(event_id.lower())
    if not event:
        raise HTTPException(status_code=404, detail="Historical event profile not found.")
    
    efficiency = run_calculation(
        event["dunbar_trust_index"],
        event["cognitive_autonomy_ratio"],
        event["resource_depletion_rate"],
        event["mortality_load_change"]
    )
    classification, action, _ = get_status_matrix(efficiency)
    return {
        "event_name": event["name"],
        "metrics_evaluated": event,
        "universal_ledger_efficiency_score": efficiency,
        "system_status": classification,
        "operational_directive": action
    }

@app.post("/audit/custom")
def audit_custom_data(payload: TelemetryPayload):
    efficiency = run_calculation(
        payload.dunbar_trust_index,
        payload.cognitive_autonomy_ratio,
        payload.resource_depletion_rate,
        payload.mortality_load_change
    )
    classification, _, _ = get_status_matrix(efficiency)
    return {
        "universal_ledger_efficiency_score": efficiency,
        "status": classification
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
