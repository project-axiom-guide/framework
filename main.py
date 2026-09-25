import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI(
    title="Project Axiom Guide: Cloud Simulation Entity",
    description="Universal Ledger Metric System (ULMS) Operational API Endpoint Engine.",
    version="1.0.0"
)

# Core Telemetry Database Layer (Pre-loaded with Chapter 11 Sandbox data)
HISTORICAL_SANDBOX = {
    "roman_republic_79ad": {
        "name": "The Roman Republic Collapse (79 AD Simulation)",
        "population_size": 45000000,
        "mortality_load_change": 0.15,      # 15% spike in preventable deaths
        "resource_depletion_rate": 1.1,     # Exceeding local regeneration biocapacity
        "dunbar_trust_index": 0.25,         # Severe internal polarization
        "intergenerational_burn_rate": 2.4, # High currency debasement passed forward
        "cognitive_autonomy_ratio": 0.30    # High tribal/demagogic delusion reliance
    },
    "singapore_1965": {
        "name": "Singapore Transition Framework (1965 Simulation)",
        "population_size": 1880000,
        "mortality_load_change": -0.45,     # 45% reduction in infant/adult mortality
        "resource_depletion_rate": 0.85,    # High efficiency resource allocation
        "dunbar_trust_index": 0.88,         # Engineered inter-ethnic social trust
        "intergenerational_burn_rate": 0.12, # Infrastructure optimized for multi-generational growth
        "cognitive_autonomy_ratio": 0.85    # High reliance on data/systems over dogma
    }
}

class TelemetryPayload(BaseModel):
    dunbar_trust_index: float
    cognitive_autonomy_ratio: float
    resource_depletion_rate: float
    mortality_load_change: float

@app.get("/")
def read_root():
    return {
        "status": "ONLINE",
        "system": "Project Axiom Guide",
        "protocol": "Universal Ledger Metric System (Chapter 11)",
        "available_sandboxes": list(HISTORICAL_SANDBOX.keys())
    }

@app.get("/audit/{event_id}")
def audit_historical_event(event_id: str):
    """Executes a system audit on pre-loaded sandbox datasets."""
    event = HISTORICAL_SANDBOX.get(event_id.lower())
    if not event:
        raise HTTPException(status_code=404, detail="Historical event profile not found in sandbox registries.")
    
    # Chapter 11 Core Equation Calculation: E = U / (R * M)
    utility = (event["dunbar_trust_index"] + event["cognitive_autonomy_ratio"]) / 2
    drain = event["resource_depletion_rate"] * (1 + event["mortality_load_change"])
    efficiency = round(utility / drain, 4)
    
    # Classification Logic Matrix
    if efficiency < 0.5:
        classification = "🟥 CRITICAL SYSTEM FAILURE: PARASITIC CODE DETECTED."
        action = "Trigger Algorithmic Quarantine & Economic Shunning Protocols (Chapter 11/12 Firewall)."
    elif 0.5 <= efficiency < 1.0:
        classification = "🟨 SYSTEM STAGNATION: BRITTLE CODE."
        action = "Deploy Micro-Niche Allocation Adjustments to optimize systemic load metrics."
    else:
        classification = "🟩 OPTIMIZED OPERATION: SYMBIOTIC COOPERATIVE FRAMEWORK."
        action = "Approve code variant; export structural design patterns to global open-source registry."

    return {
        "event_name": event["name"],
        "metrics_evaluated": event,
        "universal_ledger_efficiency_score": efficiency,
        "system_status": classification,
        "operational_directive": action
    }

@app.post("/audit/custom")
def audit_custom_data(payload: TelemetryPayload):
    """Allows global contributors to submit new event data to test against the framework."""
    utility = (payload.dunbar_trust_index + payload.cognitive_autonomy_ratio) / 2
    drain = payload.resource_depletion_rate * (1 + payload.mortality_load_change)
    efficiency = round(utility / drain, 4)
    
    return {
        "universal_ledger_efficiency_score": efficiency,
        "status": "🟥 PARASITIC" if efficiency < 0.5 else "🟨 BRITTLE" if efficiency < 1.0 else "🟩 SYMBIOTIC"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)