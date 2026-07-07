import random

class EngineeringSystemsRiskDashboard:
    def __init__(self):
        self.state_name = "Resilient_Republic"
        self.market_index = 100.0
        self.public_panic_index = 10
        self.central_bank_reserves = {
            'High_Risk_Equities': 500000000,
            'Defensive_Bonds': 300000000,
            'Gold_Reserves': 200000000
        }
        self.democratic_voting_integrity = 100.0
        self.infrastructure_blackout = False
        self.seismic_event_confirmed = False
        
        self.daily_interbank_liquidity_optimized = False
        self.daily_smart_city_traffic_saved_millions = 0
        
        print(f"=== INITIALIZING ECOSYSTEM: {self.state_name} Risk Management Center ===")
        print(f"Sovereign Portfolio: {self.central_bank_reserves}\n")

    def run_complete_state_timeline(self):
        # --- DAY 1 ---
        print("[DAY 1]: Peace-Time Status Active. Everyday operations online.")
        self.daily_interbank_liquidity_optimized = True
        print(" [DAILY WORK - BANKS]: BFS-Engine running liquidity updates.")
        self.daily_smart_city_traffic_saved_millions = random.randint(2, 5)
        print(f" [DAILY WORK - GOVT]: CGOS traffic optimization saved ${self.daily_smart_city_traffic_saved_millions}M today.")

        # --- DAY 2 ---
        print("\n [DAY 2]: CRITICAL ALERT! SEISMIC EARTHQUAKE & COORDINATED CYBER BLACKOUT HIT THE NATION! ")
        self.seismic_event_confirmed = True
        self.infrastructure_blackout = True
        print("CRITICAL HARDWARE FAULT: Commercial Telecom Towers Offline.")

        # --- DAY 3 ---
        self.public_panic_index = 95
        self.democratic_voting_integrity = 30.0
        panic_selling_multiplier = (self.public_panic_index * 0.40) + (100 - self.democratic_voting_integrity) * 0.25
        self.market_index -= panic_selling_multiplier
        print(f" [BEHAVIORAL PSYCHOLOGY]: Public Panic Index spiked to {self.public_panic_index}/100.")
        print(f"[FINANCIAL CONTAGION]: Market Index crashed to {self.market_index:.2f}")

        # --- DAY 4 ---
        print("\n [FIRMWARE OVERTAKE]: Local device hardware triggers detect total network loss...")
        print("SUCCESS: Forced device wireless transponders into P2P Mesh Grid Mode...")
        # Simulating the path array text output
        optimal_aid_corridor = ["Central_Bank_Server", "Citizen_Phone_1", "Citizen_Phone_2", "Rescue_Truck_Alpha", "Parliament"]
        print(f" CGOS RESILIENCE GRID ONLINE. Self-healed channel mapped: {optimal_aid_corridor}")
        self.democratic_voting_integrity = 99.0
        print(f"🔒 [CRYPTOGRAPHIC LOGGING]: Immutable voting data secured at {self.democratic_voting_integrity}%.")

        # --- DAY 5 ---
        print("\n [BFS CENTRAL SERVER INTERVENTION]: Isolated software executes de-risking loops.")
        capital_to_shield = self.central_bank_reserves['High_Risk_Equities'] * 0.85
        self.central_bank_reserves['High_Risk_Equities'] -= capital_to_shield
        self.central_bank_reserves['Gold_Reserves'] += (capital_to_shield * 0.50)
        self.central_bank_reserves['Defensive_Bonds'] += (capital_to_shield * 0.50)
        
        self.market_index += (self.public_panic_index * 0.30)
        self.public_panic_index -= 45
        
        print("\n=== SYSTEM STABILIZATION COMPLETE: CRISIS ECOSYSTEM CONTAINED ===")
        print(f"Shielded Sovereign Portfolio Balance: {self.central_bank_reserves}")
        print(f"Recovered Financial Market Index: {self.market_index:.2f}")
        print(f"Controlled Public Panic Level: {self.public_panic_index}/100")

# Run simulation
simulation = EngineeringSystemsRiskDashboard()
simulation.run_complete_state_timeline()
