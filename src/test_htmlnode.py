import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    
    def test_props_to_html(self):
        # Test with valid props
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

        # Test with empty props
        node = HTMLNode(props={})
        expected = ''
        self.assertEqual(node.props_to_html(), expected)

        # Test with None props
        node = HTMLNode(props=None)
        expected = ''
        self.assertEqual(node.props_to_html(), expected)

    def test_initialization(self):
        # Test with all attributes provided
        node = HTMLNode(tag="a", value="Click here", children=[], props={"href": "https://www.google.com"})
        self.assertEqual(node.tag, "a")
        self.assertEqual(node.value, "Click here")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"href": "https://www.google.com"})

        # Test with default attributes
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

    def test_repr(self):
        # Test the string representation
        node = HTMLNode(tag="div", value="Hello", children=None, props={"class": "container"})
        expected = 'HTMLNode(tag=div, value=Hello, children=None, props={\'class\': \'container\'})'
        self.assertEqual(repr(node), expected)

    def test_to_html_not_implemented(self):
        # Test that the to_html method raises NotImplementedError
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

if __name__ == '__main__':
    unittest.main()