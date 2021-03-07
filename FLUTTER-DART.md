# Flutter & Dart

### Sample main.dart for Flutter project
<details>
  <summary>Click to expand!</summary>
  

Hot-Reload works
```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: Colors.teal,
        appBar: AppBar(
          brightness: Brightness.dark,
          title: Text("Mi Card"),
          backgroundColor: Color(0xFF005F53),
        ),
        body: SafeArea(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              CircleAvatar(
                  radius: 80.0, backgroundImage: AssetImage('images/self.jpg')),
              Text("Monty Chain",
                  style: TextStyle(
                      fontSize: 40,
                      color: Colors.white,
                      fontWeight: FontWeight.bold,
                      fontFamily: "KaushanScript")),
              Text("Flutter Developer".toUpperCase(),
                  style: TextStyle(
                    fontSize: 20,
                    color: Colors.teal.shade100,
                    fontFamily: "SourceSansPro",
                    letterSpacing: 2.5,
                    fontWeight: FontWeight.bold,
                  )),
              SizedBox(
                height: 20,
                width: 150,
                child: Divider(
                  color: Colors.teal.shade100,
                ),
              ),
              Card(
                margin: EdgeInsets.symmetric(vertical: 10, horizontal: 25),
                child: ListTile(
                  leading: Icon(
                    Icons.local_phone,
                    color: Colors.teal,
                  ),
                  title: Text(
                    '+1 123 123 1234',
                    style: TextStyle(
                      color: Colors.teal.shade900,
                      fontFamily: 'SourceSansPro',
                      fontSize: 20,
                    ),
                  ),
                ),
              ),
              Card(
                margin: EdgeInsets.symmetric(vertical: 10, horizontal: 25),
                child: ListTile(
                  leading: Icon(
                    Icons.alternate_email,
                    color: Colors.teal,
                  ),
                  title: Text(
                    'email@example.com',
                    style: TextStyle(
                      color: Colors.teal.shade900,
                      fontFamily: 'SourceSansPro',
                      fontSize: 20,
                    ),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
```
Resulting app looks like this:  
![](https://i.imgur.com/QWOXAW4.png "Sample Flutter App created with the code obove")
</details>
