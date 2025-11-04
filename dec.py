import gzip
import zlib

# Read the binary data from file
with open("dump", "rb") as f:
    data = f.read()

print("Reading binary data from file...")
print(f"Data length: {len(data)} bytes")
print(f"First 16 bytes (hex): {data[:16].hex()}")
print(f"First 16 bytes (raw): {data[:16]}\n")

# Try different decompression methods
print("=" * 60)
print("Attempting decompression methods...")
print("=" * 60)

# Method 1: Raw DEFLATE (no header)
print("\n1. Trying raw DEFLATE decompression...")
try:
    decompressed = zlib.decompress(data, -zlib.MAX_WBITS)
    print("✓ SUCCESS with raw DEFLATE!")
    print(f"Decompressed size: {len(decompressed)} bytes")
    print("\nFirst 1000 characters of decompressed data:")
    print("-" * 60)
    try:
        text = decompressed.decode("utf-8")
        print(text[:1000])
    except Exception:
        print(decompressed[:1000])
    print("-" * 60)

    # Save to file
    with open("decompressed_output.txt", "wb") as f:
        f.write(decompressed)
    print("\n✓ Full decompressed data saved to 'decompressed_output.txt'")

except Exception as e:
    print(f"✗ Failed: {e}")

# Method 2: zlib decompression (with header)
print("\n2. Trying zlib decompression (with header)...")
try:
    decompressed = zlib.decompress(data)
    print("✓ SUCCESS with zlib!")
    print(f"Decompressed size: {len(decompressed)} bytes")
    print("\nFirst 1000 characters:")
    print("-" * 60)
    try:
        text = decompressed.decode("utf-8")
        print(text[:1000])
    except Exception:
        print(decompressed[:1000])
    print("-" * 60)

    # Save to file if not already saved
    try:
        with open("decompressed_output_zlib.txt", "wb") as f:
            f.write(decompressed)
        print("\n✓ Full decompressed data saved to 'decompressed_output_zlib.txt'")
    except Exception:
        pass

except Exception as e:
    print(f"✗ Failed: {e}")

# Method 3: gzip decompression
print("\n3. Trying gzip decompression...")
try:
    decompressed = gzip.decompress(data)
    print("✓ SUCCESS with gzip!")
    print(f"Decompressed size: {len(decompressed)} bytes")
    print("\nFirst 1000 characters:")
    print("-" * 60)
    try:
        text = decompressed.decode("utf-8")
        print(text[:1000])
    except Exception:
        print(decompressed[:1000])
    print("-" * 60)

    # Save to file if not already saved
    try:
        with open("decompressed_output_gzip.txt", "wb") as f:
            f.write(decompressed)
        print("\n✓ Full decompressed data saved to 'decompressed_output_gzip.txt'")
    except Exception:
        pass

except Exception as e:
    print(f"✗ Failed: {e}")

print("\n" + "=" * 60)
print("Decompression attempts complete")
print("=" * 60)
