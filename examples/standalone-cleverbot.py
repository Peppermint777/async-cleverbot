"""
MIT License

Copyright (c) 2018-2021 chr1s

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# Example Cleverbot standalone program.

import asyncio
import async_cleverbot as ac

cleverbot = ac.Cleverbot("API key", context=ac.DictContext())


async def main():
    while True:
        q = input("Ask me a question by typing it and pressing enter! >>> ")
        try:
            r = await cleverbot.ask(q, __name__)
        except ac.InvalidKey:
            print("An error has occurred. The API key provided was not valid.")
            break
        except ac.APIDown:
            print("I have to sleep sometimes. Please ask later!")
            break
        else:
            print(r.text)
    await cleverbot.close()


asyncio.get_event_loop().run_until_complete(main())
