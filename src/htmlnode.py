# htmlnode.py
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        """Generates the HTML representation of the node."""
        raise NotImplementedError

    def props_to_html(self):
        """Converts the props dictionary into an HTML attribute string."""
        if not self.props:  # Handle None or empty dictionary
            return ""
        res = ""
        for key, value in self.props.items():
            res += f' {key}="{value}"'
        return res

    def __repr__(self):
        """Returns a string representation of the HTMLNode instance."""
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"