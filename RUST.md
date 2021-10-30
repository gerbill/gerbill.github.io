# Rust Notes
## Implementing Debug for enum and struct
Here I implemented debug for enum and struct

```rust
use std::fmt;

enum Color {
    Red,
    Green,
    Blue,
}

impl fmt::Debug for Color {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        let printable = match *self {
            Color::Red => "red",
            Color::Blue => "blue",
            Color::Green => "green",
        };
        write!(f, "{}", printable)
    }
}

struct Items {
    name: String,
    color: Color,
    quantity: u8,
    weight: f64
}

impl fmt::Debug for Items {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("Items")
            .field("name", &self.name)
            .field("color", &self.color)
            .field("quantity", &self.quantity)
            .field("weight", &self.weight)
            .finish()
    }
}

fn main() {
    let apple = Items{
        name: String::from("apple"),
        color: Color::Red,
        quantity: 10,
        weight: 10.5,
    };
    println!("{:?}", apple);
}

```

## Wait for user input
```rust
use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).expect("error: unable to read user input");
}
```
