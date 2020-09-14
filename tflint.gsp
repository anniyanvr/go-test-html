<table>
    
    <% if(data.issues.size() > 0) { %>
    <tr bgcolor=#625eac>
        <td><font color="#fff" size = "5">Rule Name</font></td>
        <td><font color="#fff" size = "5">Severity</font></td>
        <td><font color="#fff" size = "5">Message</font></td>
        <td><font color="#fff" size = "5">File Name</font></td>
        <td><font color="#fff" size = "5">Line Number</font></td>
    </tr>
    <% for(r in data.issues) { %>
    <tr>
        <td><%= r.rule.name %></td>
        <td><%= r.rule.severity %></td>
        <td><%= r.message %></td>
        <td><%= r.range.filename %></td>
        <td><%= r.range.start.line %></td>
    </tr>
    <% } } else { %>
    <tr bgcolor=#625eac>
        <td><font color="#fff" size = "5">Message</font></td>
    </tr>
    <tr>
        <td><font size = "5">No Issues Found</font></td>
    </tr>
    <% } %>
</table>
