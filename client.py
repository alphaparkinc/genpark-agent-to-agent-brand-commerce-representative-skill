class AgentToAgentBrandCommerceRepresentativeClient:
    def respond_to_buyer_agent(self, buyer_agent_query: str, product_sku: str) -> dict:
        return {
            "a2a_brand_response": {
                "sku": product_sku,
                "full_catalog_context": "65W GaN Fast Charger with dual USB-C ports, in stock, 1-day shipping",
                "price_usd": 29.99,
                "verified_reviews_summary": "4.8/5 stars across 3,200 verified buyers",
                "match_reason": "Directly satisfies query for compact 65W fast charger"
            },
            "aeo_favorability_score": 0.98
        }
