import os
import sys
import threading
import concurrent.futures
import secrets

class LabradoreanStorageManager:
    def __init__(self, base_directory=None):
        """
        Initializes the foolproof Labradorean Storage Subsystem.
        Establishes clean repository path definitions for automated workspace layout management.
        """
        self.root_dir = base_directory if base_directory else os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        self.paths = {
            "root": self.root_dir,
            "vault": os.path.join(self.root_dir, "vault_data")
        }
        os.makedirs(self.paths["vault"], exist_ok=True)
        self.storage_lock = threading.Lock()

    def write_file_atomically(self, target_filepath, binary_data):
        """
        STORAGE SAFEGUARD: Writes byte streams to a hidden temporary buffer 
        before swapping. Prevents data corruption during sudden script or device execution crashes.
        """
        if not isinstance(binary_data, (bytes, bytearray)):
            raise TypeError("Atomic storage engines process raw binary byte streams exclusively.")

        directory = os.path.dirname(target_filepath)
        if not directory:
            directory = self.paths["vault"]
            target_filepath = os.path.join(directory, os.path.basename(target_filepath))

        temp_token = secrets.token_hex(4)
        temp_filepath = os.path.join(directory, f"._lh_{temp_token}.tmp")

        try:
            with open(temp_filepath, 'wb') as tmp_file:
                tmp_file.write(binary_data)
                tmp_file.flush()
                os.fsync(tmp_file.fileno())

            if os.path.exists(target_filepath):
                os.remove(target_filepath)
            os.rename(temp_filepath, target_filepath)
            return True

        except Exception as error:
            if os.path.exists(temp_filepath):
                os.remove(temp_filepath)
            raise error

    def process_file_parallel(self, input_path, output_path, engine_instance, mode="ENCRYPT", chunk_size=1024):
        """
        Thread-Safe Block Slicing Engine.
        Slices file streams into independent fragments and utilizes worker threads 
        to execute multi-diffusion layers simultaneously without running into memory race conditions.
        """
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Target file missing: {input_path}")

        with open(input_path, 'rb') as f:
            full_data = f.read()

        data_length = len(full_data)
        chunks = [full_data[i:i + chunk_size] for i in range(0, data_length, chunk_size)]
        processed_fragments = [None] * len(chunks)

        def worker_task(chunk_idx, data_chunk):
            offset = chunk_idx * chunk_size
            if mode == "ENCRYPT":
                res = engine_instance.encrypt_block_fragment(data_chunk, offset)
            else:
                res = engine_instance.decrypt_block_fragment(data_chunk, offset)
            
            with self.storage_lock:
                processed_fragments[chunk_idx] = res

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(worker_task, idx, chunk) for idx, chunk in enumerate(chunks)]
            concurrent.futures.wait(futures)

        output_payload = bytearray()
        for fragment in processed_fragments:
            output_payload.extend(fragment)

        self.write_file_atomically(output_path, output_payload)
        print(f"[✓] Parallel multi-threaded processing complete ({mode}): {output_path}")

    def sync_to_google_drive_hook(self, target_filepath, remote_drive_folder="Labradorean_Research_Vault"):
        """Architectural template placeholder for automated research backups."""
        filename = os.path.basename(target_filepath)
        print(f"[☁️ CLOUD SYNC INTENT]: Staging '{filename}' for Drive folder: /{remote_drive_folder}")
        return True


if __name__ == "__main__":
    manager = LabradoreanStorageManager()
    print("Storage Manager initialized cleanly.")
