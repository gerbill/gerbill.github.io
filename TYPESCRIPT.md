# TypeScrypt snippets


## Read large file line by line generator

```typescript
import * as fs from "fs";
import * as readline from "readline";

async function* readLines(filePath: string) : AsyncGenerator{
  const fileStream = fs.createReadStream(filePath)
  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity
  })
  for await (const line of rl) {
    yield line
  }
}


async function main() {
  let counter = 0
  for await (let line of readLines('./domain-list.txt')) {
    counter++
    if (counter % 1_000_000 === 0) {
      console.log(counter);
    }
  }
}

main().then()
```
