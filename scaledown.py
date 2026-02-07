class Scaledown:
    @staticmethod
    def compress(data, factor=10):
        """
        Compress data by sampling every `factor` points.
        """
        if not data:
            return data

        # Simple and safe downsampling
        compressed = data[::factor]

        print(f"Scaledown: compressed {len(data)} -> {len(compressed)} points")
        return compressed
