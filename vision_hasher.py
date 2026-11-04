import hashlib

class VisionHasher:
    @staticmethod
    def generate_perceptual_hash(image_path_or_bytes):
        """
        Simulates generating a perceptual image hash (similar to pHash / dHash) 
        to track visual similarities across profile images.
        """
        if isinstance(image_path_or_bytes, str):
            # If a string identifier/path is passed
            hasher = hashlib.sha256(image_path_or_bytes.encode())
        else:
            hasher = hashlib.sha256(image_path_or_bytes)
            
        # Return a normalized hexadecimal visual signature
        return f"vhash_{hasher.hexdigest()[:16]}"

    @staticmethod
    def compare_visual_similarity(hash_a, hash_b):
        """
        Compares two visual hashes to check if a profile image has been stolen/cloned.
        Returns a similarity score between 0.0 (completely different) and 1.0 (identical clone).
        """
        if hash_a == hash_b:
            return 1.0  # Identical image match (stolen photo clone)
            
        # Basic Hamming / character distance simulation for hackathon demo
        matching_chars = sum(c1 == c2 for c1, c2 in zip(hash_a, hash_b))
        similarity = matching_chars / max(len(hash_a), len(hash_b))
        
        return round(similarity, 2)