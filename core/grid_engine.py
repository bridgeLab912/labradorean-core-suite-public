import os
import sys
import math

class LabradoreanGridEngine:
    def __init__(self):
        """
        Initializes the Core 9x12 Labradorean Matrix Engine.
        Standardizes the row-column geometry bounds to enforce coordinate invariance.
        """
        self.rows = 9
        self.cols = 12
        self.total_elements = self.rows * self.cols  # Exact 108 macro grid space
        self.active_channel_count = 36
        self.active_channels = self._initialize_36_active_channels()

    def _initialize_36_active_channels(self):
        """
        Maps out the exact 36 mathematically active coordinate channels 
        within the 108 macro grid space based on index step invariants.
        """
        channels = []
        for i in range(1, self.active_channel_count + 1):
            channel_id = (i * 3) % self.total_elements
            if channel_id == 0:
                channel_id = self.total_elements
            channels.append(channel_id)
        return sorted(list(set(channels)))

    def map_integer_to_coordinate(self, value):
        """
        Applies a strict column-major sequential distribution layout.
        Maps any real integer straight to its exact (row, column) coordinate index.
        """
        if value <= 0:
            raise ValueError("The grid engine processes positive integer spaces sequentially.")
            
        relative_idx = (value - 1) % self.total_elements
        row = (relative_idx % self.rows) + 1
        col = (relative_idx // self.rows) + 1
        return (row, col)

    def calculate_sequence_velocity(self, number_sequence):
        """
        Tracks the consecutive 'hops' of a sequence across the 36 active channels.
        Returns a high-entropy tracking profile used for keystream seeds.
        """
        velocity_profile = []
        for val in number_sequence:
            relative_pos = ((val - 1) % self.total_elements) + 1
            
            if relative_pos in self.active_channels:
                channel_weight = self.active_channels.index(relative_pos) + 1
                hop_velocity = (val * channel_weight) % 256
                velocity_profile.append(hop_velocity)
                
        if len(velocity_profile) < 36:
            fallback_seed = 0x7F
            while len(velocity_profile) < 36:
                fallback_seed = (fallback_seed * 33) % 256
                velocity_profile.append(fallback_seed)
                
        return velocity_profile[:36]

    def extract_prime_power_bounds(self, upper_bound):
        """
        Locates and tracks higher prime powers (p², p³) distributed across the 
        active matrix tracks up to specified scale milestones.
        """
        limit = int(math.isqrt(upper_bound)) + 1
        sieve = [True] * limit
        primes = []
        
        for p in range(2, limit):
            if sieve[p]:
                primes.append(p)
                for i in range(p*p, limit, p):
                    sieve[i] = False
                    
        matrix_bounds_manifest = []
        
        for p in primes:
            p2 = p * p
            p3 = p * p * p
            
            if p2 <= upper_bound:
                r2, c2 = self.map_integer_to_coordinate(p2)
                matrix_bounds_manifest.append({"type": "p^2", "value": p2, "coord": (r2, c2)})
            if p3 <= upper_bound:
                r3, c3 = self.map_integer_to_coordinate(p3)
                matrix_bounds_manifest.append({"type": "p^3", "value": p3, "coord": (r3, c3)})
                
        return matrix_bounds_manifest


if __name__ == "__main__":
    print("=== Labradorean Core 9x12 Grid Math Engine Functional Test ===")
    engine = LabradoreanGridEngine()
    print(f"Active channels initialized: {len(engine.active_channels)} / 36")
