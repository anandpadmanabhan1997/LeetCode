import asyncio
import random

# Simulate an async API call
async def fetch_data(source: str):
    delay = random.uniform(1, 3)  # Simulate network delay
    print(f"Fetching from {source}...")
    await asyncio.sleep(delay)
    print(f"Done fetching from {source} (delay: {delay:.2f}s)")
    return f"{source} data"

# Main coroutine to run all tasks concurrently
async def main():
    sources = ["Patient Records", "Warehouse", "Billing", "Lab Results"]
    
    # Create a list of coroutines
    tasks = [fetch_data(src) for src in sources]
    
    # Run all coroutines concurrently
    results = await asyncio.gather(*tasks)
    
    print("\nAll data fetched:")
    for result in results:
        print(result)

# Run the event loop
asyncio.run(main())
