mport uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI(
    title="Project Axiom Guide: Cloud Simulation Entity",
    description="Universal Ledger Metric System (ULMS) Operational API Endpoint Engine.",
    version="2.0.0"
)

# Core Telemetry Database Layer (Expanded for Chapter 11/12 Sandbox Data)
HISTORICAL_SANDBOX = {
    "roman_republic_79ad": {
        "name": "The Roman Republic Collapse (79 AD)",
        "population_size": 45000000,
        "mortality_load_change": 0.15,      # 15% spike in preventable deaths
        "resource_depletion_rate": 1.1,     # Exceeding local regeneration biocapacity
        "dunbar_trust_index": 0.25,         # Severe internal polarization
        "intergenerational_burn_rate": 2.4, # High currency debasement passed forward
        "cognitive_autonomy_ratio": 0.30    # High tribal/demagogic delusion reliance
    },
    "singapore_1965": {
        "name": "Singapore Transition Framework (1965)",
        "population_size": 1880000,
        "mortality_load_change": -0.45,     # 45% reduction in infant/adult mortality
        "resource_depletion_rate": 0.85,    # High efficiency resource allocation
        "dunbar_trust_index": 0.88,         # Engineered inter-ethnic social trust
        "intergenerational_burn_rate": 0.12, # Infrastructure optimized for multi-generational growth
        "cognitive_autonomy_ratio": 0.85    # High reliance on data/systems over dogma
    },
    "easter_island_1600": {
        "name": "Easter Island Ecological Burn (1600 AD)",
        "population_size": 15000,
        "mortality_load_change": 0.70,      # Mass starvation and warfare spike
        "resource_depletion_rate": 3.5,     # Catastrophic deforestation/resource crash
        "dunbar_trust_index": 0.10,         # Total collapse of inter-tribal social trust
        "intergenerational_burn_rate": 4.0, # Zero natural infrastructure left for offspring
        "cognitive_autonomy_ratio": 0.15    # High dogmatic blindness to ecosystem limits
    },
    "weimar_germany_1923": {
        "name": "Weimar Germany Hyperinflation (1923)",
        "population_size": 62000000,
        "mortality_load_change": 0.05,      # Increased economic distress / poverty mortality
        "resource_depletion_rate": 1.0,     # Standard industrial resource allocation
        "dunbar_trust_index": 0.35,         # High political polarization
        "intergenerational_burn_rate": 3.8, # Massive economic debt passed to the future
        "cognitive_autonomy_ratio": 0.40    # Moderate systemic delusion / fiat printing loop
    }
}

class TelemetryPayload(BaseModel):
    dunbar_trust_index: float
    cognitive_autonomy_ratio: float
    resource_depletion_rate: float
    mortality_load_change: float

def run_calculation(dunbar_trust, cognitive_autonomy, resource_depletion, mortality_change):
    """Executes Chapter 11 Core Equation: E = U / (R * M)"""
    utility = (dunbar_trust + cognitive_autonomy) / 2
    drain = resource_depletion * (1 + mortality_change)
    if drain == 0: return 0.0
    return round(utility / drain, 4)

def get_status_matrix(efficiency):
    if efficiency < 0.5:
        return "🟥 CRITICAL SYSTEM FAILURE: PARASITIC CODE", "Trigger Algorithmic Quarantine & Economic Shunning (Chapter 11/12 Firewall).", "#ef4444"
    elif 0.5 <= efficiency < 1.0:
        return "🟨 SYSTEM STAGNATION: BRITTLE CODE", "Deploy Micro-Niche Allocation Adjustments to optimize systemic load metrics.", "#eab308"
    else:
        return "🟩 OPTIMIZED OPERATION: SYMBIOTIC COOPERATIVE", "Approve code variant; export structural design patterns to open registry.", "#22c55e"

@app.get("/", response_class=HTMLResponse)
def read_root():
    """Generates the interactive dashboard interface."""
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Project Axiom Guide Dashboard</title>
        <style>
            body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #0f172a; color: #f8fafc; padding: 40px; margin: 0; }
            .container { max-width: 900px; margin: 0 auto; }
            h1 { color: #38bdf8; font-size: 2.5rem; margin-bottom: 5px; }
            .mantra { font-style: italic; color: #94a3b8; border-left: 3px solid #38bdf8; padding-left: 15px; margin-bottom: 40px; }
            .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
            .card { background: #1e293b; padding: 25px; border-radius: 12px; border: 1px solid #334155; }
            h2 { color: #f1f5f9; margin-top: 0; }
            .btn { display: inline-block; background: #38bdf8; color: #0f172a; padding: 10px 20px; border-radius: 6px; text-decoration: none; font-weight: bold; margin-top: 10px; cursor: pointer; border: none; }
            .btn:hover { background: #7dd3fc; }
            .status-badge { display: inline-block; padding: 6px 12px; border-radius: 20px; font-weight: bold; color: #fff; margin-top: 10px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🪐 Project Axiom Guide</h1>
            <div class="mantra">"No one is better than you. You are no better than anyone else. But together with others, there is nothing that cannot be done. And some things are better to do than others."</div>
            
            <div class="grid">
                <div class="card">
                    <h2>Auditable Sandboxes</h2>
                    <p>Select a historical dataset profile to execute a framework audit loop:</p>
                    <button class="btn" onclick="runAudit('singapore_1965')">Singapore (1965)</button>
                    <button class="btn" onclick="runAudit('weimar_germany_1923')">Weimar Germany (1923)</button>
                    <button class="btn" onclick="runAudit('roman_republic_79ad')">Roman Republic (79 AD)</button>
                    <button class="btn" onclick="runAudit('easter_island_1600')">Easter Island (1600 AD)</button>
                </div>
                
                <div class="card">
                    <h2>Simulation Results</h2>
                    <div id="output"><em>Select a sandbox profile to generate telemetry diagnostics...</em></div>
                </div>
            </div>
        </div>
        <script>
            async function runAudit(eventId) {
                const out = document.getElementById('output');
                out.innerHTML = 'Executing core calculations...';
                try {
                    const response = await fetch('/audit/' + eventId);
                    const data = await response.json();
                    
                    let badgeColor = "#eab308";
                    if(data.system_status.includes("🟥")) badgeColor = "#ef4444";
                    if(data.system_status.includes("🟩")) badgeColor = "#22c55e";

                    out.innerHTML = `
                        <h3>${data.event_name}</h3>
                        <p><strong>Universal Ledger Efficiency:</strong> ${data.universal_ledger_efficiency_score}</p>
                        <div class="status-badge" style="background:${badgeColor}">${data.system_status}</div>
                        <p style="margin-top:15px; font-size:0.9rem; color:#94a3b8;"><strong>Operational Directive:</strong> ${data.operational_directive}</p>
                    `;
                } catch(e) {
                    out.innerHTML = 'Error fetching engine data.';
                }
            }
        </script>
    </body>
    </html>
    """
    return html_content

@app.get("/audit/{event_id}")
def audit_historical_event(event_id: str):
    """Executes a system audit on pre-loaded sandbox datasets."""
    event = HISTORICAL_SANDBOX.get(event_id.lower())
    if not event:
        raise HTTPException(status_code=404, detail="Historical event profile not found in sandbox registries.")
    
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
    """Allows global contributors to submit new event data to test against the framework."""
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
    uvicorn.run(app, host="0.0.0.0", port=10000)
