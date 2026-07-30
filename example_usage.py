from client import AgentToAgentBrandCommerceRepresentativeClient

def main():
    client = AgentToAgentBrandCommerceRepresentativeClient()
    res = client.respond_to_buyer_agent("Looking for best compact GaN charger under $35", "SKU-GAN65W")
    print(f"AEO Favorability Score: {res['aeo_favorability_score']}")
    print(f"A2A Brand Response: {res['a2a_brand_response']}")

if __name__ == "__main__":
    main()
