# JavaScript


### Multiple async requests

```javascript
rPromises = [...Array(100).keys()].map((i) =>
  // prettier-ignore
  fetch(`https://jsonplaceholder.typicode.com/posts/${i + 1}`)
    .then(r => r.json())
    .then(data => console.log(`Completed one: ${new Date().getTime()}`))
    .catch((err) => console.error(`We've got and error over here: ${err}`))
);

// prettier-ignore
Promise.allSettled(rPromises)
  .then(() => console.log(`Completed all: ${new Date().getTime()}`))
  .then(() => console.log('After all is completed'))

```
