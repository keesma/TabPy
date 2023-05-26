def test_init(self):
        client = Client("http://example.com:9004")

        self.assertEqual(client._endpoint, "http://example.com:9004")

        client = Client("http://example.com/", 10.0)

        self.assertEqual(client._endpoint, "http://example.com/")

        client = Client(endpoint="https://example.com/", query_timeout=-10.0)

        self.assertEqual(client._endpoint, "https://example.com/")
        self.assertEqual(client.query_timeout, 0.0)

        # valid name tests
        with self.assertRaises(ValueError):
            Client("")
        with self.assertRaises(TypeError):
            Client(1.0)
        with self.assertRaises(ValueError):
            Client("*#")
        with self.assertRaises(TypeError):
            Client()
        with self.assertRaises(ValueError):
            Client("http:/www.example.com/")
        with self.assertRaises(ValueError):
