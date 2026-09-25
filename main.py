import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Dict, Any

app = FastAPI(
    title="Project Axiom Guide: Cloud Simulation Entity",
    description="Universal Ledger Metric System (ULMS) Operational API Endpoint Engine.",
    version="3.0.0"
)

HISTORICAL_SANDBOX = {
    "roman_republic_79ad": {
        "name": "The Roman Republic Collapse (79 AD)",
        "population_size": 45000000,
        "mortality_load_change": 0.15,
        "resource_depletion_rate": 1.1,
        "dunbar_trust_index": 0.25,
        "intergenerational_burn_rate": 2.4,
        "cognitive_autonomy_ratio": 0.30
    },
    "singapore_1965": {
        "name": "Singapore Transition Framework (1965)",
        "population_size": 1880000,
        "mortality_load_change": -0.45,
        "resource_depletion_rate": 0.85,
        "dunbar_trust_index": 0.88,
        "intergenerational_burn_rate": 0.12,
        "cognitive_autonomy_ratio": 0.85
    },
    "easter_island_1600": {
        "name": "Easter Island Ecological Burn (1600 AD)",
        "population_size": 15000,
        "mortality_load_change": 0.70,
        "resource_depletion_rate": 3.5,
        "dunbar_trust_index": 0.10,
        "intergenerational_burn_rate": 4.0,
        "cognitive_autonomy_ratio": 0.15
    },
    "weimar_germany_1923": {
        "name": "Weimar Germany Hyperinflation (1923)",
        "population_size": 62000000,
        "mortality_load_change": 0.05,
        "resource_depletion_rate": 1.0,
        "dunbar_trust_index": 0.35,
        "intergenerational_burn_rate": 3.8,
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

@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Project Axiom Guide Dashboard</title>
        <style>
            body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background: #0f172a; color: #f8fafc; padding: 40px; margin: 0; }
            .container { max-width: 1000px; margin: 0 auto; }
            h1 { color: #38bdf8; font-size: 2.5rem; margin-bottom: 5px; }
            .mantra { font-style: italic; color: #94a3b8; border-left: 3px solid #38bdf8; padding-left: 15px; margin-bottom: 40px; }
            .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 25px; margin-bottom: 25px; }
            .card { background: #1e293b; padding: 25px; border-radius: 12px; border: 1px solid #334155; }
            .card-full { background: #1e293b; padding: 25px; border-radius: 12px; border: 1px solid #334155; margin-top: 25px; }
            h2 { color: #f1f5f9; margin-top: 0; border-bottom: 1px solid #334155; padding-bottom: 10px; }
            .btn { display: inline-block; background: #38bdf8; color: #0f172a; padding: 10px 20px; border-radius: 6px; text-decoration: none; font-weight: bold; margin-top: 10px; cursor: pointer; border: none; margin-right: 5px; }
            .btn:hover { background: #7dd3fc; }
            .status-badge { display: inline-block; padding: 6px 12px; border-radius: 20px; font-weight: bold; color: #fff; margin-top: 10px; }
            .slider-group { margin-bottom: 20px; }
            .slider-group label { display: block; font-weight: bold; margin-bottom: 5px; color: #cbd5e1; }
            .slider-container { display: flex; align-items: center; gap: 15px; }
            input[type=range] { flex: 1; accent-color: #38bdf8; }
            .slider-val { width: 50px; text-align: right; font-family: monospace; font-size: 1.1rem; color: #38bdf8; }
            .description { font-size: 0.85rem; color: #94a3b8; margin-top: 2px; }
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
                    <h2>Simulation Outputs</h2>
                    <div id="output"><em>Select a sandbox profile or use the calculator below to generate telemetry diagnostics...</em></div>
                </div>
            </div>

            <div class="card-full">
                <h2>Chapter 11: Predictive Sandbox Calculator</h2>
                <p style="color: #94a3b8; margin-bottom: 25px;">Manually slide parameters to test a custom hypothetical society configuration against the global life-support formulas:</p>
                
                <div class="grid">
                    <div>
                        <div class="slider-group">
                            <label>Dunbar Trust Index (Social Mortar)</label>
                            <div class="slider-container">
                                <input type="range" id="trust" min="0.0" max="1.0" step="0.01" value="0.50" oninput="updateVal('trust_val', this.value); calculateCustom();">
                                <span class="slider-val" id="trust_val">0.50</span>
                            </div>
                            <div class="description">Scale of peaceful, unforced cooperation between strangers (0 = Total Polarization, 1 = Perfect Trust).</div>
                        </div>

                        <div class="slider-group">
                            <label>Cognitive Autonomy Ratio (Reality Verification)</label>
                            <div class="slider-container">
                                <input type="range" id="autonomy" min="0.0" max="1.0" step="0.01" value="0.50" oninput="updateVal('autonomy_val', this.value); calculateCustom();">
                                <span class="slider-val" id="autonomy_val">0.50</span>
                            </div>
                            <div class="description">The population's reliance on physical data over dogmatic/parasitic delusions (1 = Fully Rational).</div>
                        </div>
                    </div>

                    <div>
                        <div class="slider-group">
                            <label>Resource Depletion Rate (Ecological Load)</label>
                            <div class="slider-container">
                                <input type="range" id="depletion" min="0.1" max="5.0" step="0.1" value="1.0" oninput="updateVal('depletion_val', this.value); calculateCustom();">
                                <span class="slider-val" id="depletion_val">1.0</span>
                            </div>
                            <div class="description">Consumption relative to Earth's natural replenishment pace (Values > 1.0 indicate an active ecological deficit).</div>
                        </div>

                        <div class="slider-group">
                            <label>Mortality Load Change (Preventable Deaths)</label>
                            <div class="slider-container">
                                <input type="range" id="mortality" min="-0.9" max="2.0" step="0.05" value="0.00" oninput="updateVal('mortality_val', this.value); calculateCustom();">
                                <span class="slider-val" id="mortality_val">0.00</span>
                            </div>
                            <div class="description">Shift in regional mortality due to system infrastructure adjustments (-0.5 = 50% Fewer Deaths, 1.0 = Deaths Doubled).</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <script>
            function updateVal(id, val) {
                document.getElementById(id).innerText = parseFloat(val).toFixed(2);
            }

            function renderOutput(title, score, status, directive) {
                const out = document.getElementById('output');
                let badgeColor = "#eab308";
                if(status.includes("🟥")) badgeColor = "#ef4444";
                if(status.includes("🟩")) badgeColor = "#22c55e";

                out.innerHTML = `
                                  <h3>${title}</h3>
                    <p><strong>Universal Ledger Efficiency Score:</strong> ${score}</p>
                    <div class="status-badge" style="background:${badgeColor}">${status}</div>
                    <p style="margin-top:15px; font-size:0.9rem; color:#94a3b8;"><strong>Operational Directive:</strong> ${directive}</p>
                `;
            }

            async function runAudit(eventId) {
                const out = document.getElementById('output');
                out.innerHTML = 'Executing core calculations...';
                try {
                    const response = await fetch('/audit/' + eventId);
                    const data = await response.json();
                    
                    renderOutput(data.event_name, data.universal_ledger_efficiency_score, data.system_status, data.operational_directive);

                    document.getElementById('trust').value = data.metrics_evaluated.dunbar_trust_index;
                    document.getElementById('autonomy').value = data.metrics_evaluated.cognitive_autonomy_ratio;
                    document.getElementById('depletion').value = data.metrics_evaluated.resource_depletion_rate;
                    document.getElementById('mortality').value = data.metrics_evaluated.mortality_load_change;

                    updateVal('trust_val', data.metrics_evaluated.dunbar_trust_index);
                    updateVal('autonomy_val', data.metrics_evaluated.cognitive_autonomy_ratio);
                    updateVal('depletion_val', data.metrics_evaluated.resource_depletion_rate);
                    updateVal('mortality_val', data.metrics_evaluated.mortality_load_change);
                } catch(e) {
                    out.innerHTML = 'Error fetching engine data.';
                }
            }

            async function calculateCustom() {
                const trust = parseFloat(document.getElementById('trust').value);
                const autonomy = parseFloat(document.getElementById('autonomy').value);
                const depletion = parseFloat(document.getElementById('depletion').value);
                const mortality = parseFloat(document.getElementById('mortality').value);

                try {
                    const response = await fetch('/audit/custom', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({
                            dunbar_trust_index: trust,
                            cognitive_autonomy_ratio: autonomy,
                            resource_depletion_rate: depletion,
                            mortality_load_change: mortality
                        })
                    });
                    const data = await response.json();

                    let directive = "Maintain active sandbox parameter constraints.";
                    if (data.status.includes("🟥")) directive = "Trigger Algorithmic Quarantine & Economic Shunning (Chapter 11/12 Firewall).";
                    if (data.status.includes("🟨")) directive = "Deploy Micro-Niche Allocation Adjustments to optimize systemic load metrics.";
                    if (data.status.includes("🟩")) directive = "Approve code variant; export structural design patterns to open registry.";

                    renderOutput("Custom Hypothesis Configuration", data.universal_ledger_efficiency_score, data.status, directive);
                } catch(e) {
                    document.getElementById('output').innerHTML = 'Calculation failure inside cloud engine routing.';
                }
            }
        </script>
    </body>
    </html>
    """
    return html_content

@app.get("/audit/{event_id}")
def audit_historical_event(event_id: str):
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
