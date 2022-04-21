import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

Future<String> scrapeURL(String url) async {
  var response = await http.post(
    Uri.parse('http://localhost:8000/webscraperapi/'),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode(<String, String>{
      'url': url,
    }),
  );

  if (response.statusCode == 200) {
    return "Success";
  } else {
    return "Failure";
  }
}

Future<WordQuery> fetchWordResults(String word) async {
  final response = await http.post(
    Uri.parse("http://localhost:8000/webscraperapi/"),
    headers: <String, String>{
      'Content-Type': 'application/json; charset=UTF-8',
    },
    body: jsonEncode(<String, String>{
      'word': word,
    }),
  );
  if (response.statusCode == 200) {
    return WordQuery.fromJson(jsonDecode(response.body));
  } else {
    return WordQuery();
  }
}

class WordQuery {
  final String word;
  final int count;
  final List<String> urls;

  const WordQuery(
      {this.word = "", this.count = 0, this.urls = const <String>[]});

  factory WordQuery.fromJson(Map<String, dynamic> json) {
    return WordQuery(
      count: json['count'],
      urls: json['urls'],
    );
  }
}

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  static const String _title = 'Web Scraper';

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: _title,
      theme: ThemeData.dark(),
      home: MyStatefulWidget(title: _title),
    );
  }
}

class MyStatefulWidget extends StatefulWidget {
  const MyStatefulWidget({Key? key, required this.title}) : super(key: key);

  final String title;

  @override
  State<MyStatefulWidget> createState() => _MyStatefulWidgetState();
}

class _MyStatefulWidgetState extends State<MyStatefulWidget> {
  late TextEditingController _controller;
  late Future<WordQuery> _futureWordQuery;
  late Future<String> _futureScrapeURL;

  @override
  void initState() {
    super.initState();
    _controller = TextEditingController();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Center(child: Text(widget.title)),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            const Text('Web Scraper',
                style: TextStyle(
                  fontSize: 24,
                  fontWeight: FontWeight.bold,
                  color: Colors.greenAccent,
                )),
            TextField(
              decoration: const InputDecoration(
                border: OutlineInputBorder(),
                hintText:
                    'Enter URL to scrape or word to query from last scrape',
              ),
              textAlign: TextAlign.center,
              controller: _controller,
            ),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                ElevatedButton(
                  onPressed: () {
                    setState(() {
                      _futureScrapeURL = scrapeURL(_controller.text);
                      if (_futureScrapeURL == "Success") {
                        _controller.text = "Successfully Scraped";
                      } else {
                        _controller.text = "Failed to Scrape";
                      }
                    });
                  },
                  child: const Text('Scrape URL'),
                ),
                ElevatedButton(
                    onPressed: () {
                      setState(() {
                        _futureWordQuery =
                            fetchWordResults(_controller.text.trim());
                        _controller.text = _futureWordQuery.toString();
                      });
                    },
                    child: const Text('Query Scrape Results')),
              ],
            )
          ],
        ),
      ),
    );
  }
}
