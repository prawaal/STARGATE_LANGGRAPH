class ETFMapper:

    def __init__(
        self,
        discovery_engine,
        validator
    ):

        self.discovery_engine = (
            discovery_engine
        )

        self.validator = validator

    def build_mappings(
        self,
        expanded_ontology
    ):

        mappings = []

        for node in expanded_ontology:

            category = node["category"]

            print(
                f"\nDiscovering ETFs "
                f"for {category}"
            )

            result = (
                self.discovery_engine
                .discover_etfs(
                    category,
                    node["subcategories"]
                )
            )

            valid_etfs = []

            for etf in result[
                "candidate_etfs"
            ]:

                ticker = etf["ticker"]

                is_valid = (
                    self.validator
                    .validate_etf(
                        ticker
                    )
                )

                if is_valid:

                    valid_etfs.append(etf)

            mappings.append({

                "category": category,

                "etfs": valid_etfs
            })

        return mappings