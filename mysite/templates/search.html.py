{% include 'labs_form.html' %}

            {% if result %}
                <p>
                    You searched for: {{search}}
                </p>
                <br/><br/><br/>
                <table>
                    <tr>
                        <th>
                            Translation
                        </th>
                        <th>
                            Translation Score
                        </th>
                    </tr>
                    <tr>
                        {% for translation, score in result %}
                            <tr>
                                <td>
                                    {{ translation }}
                                </td>
                                <td>
                                    {{ score }}
                                </td>
                            </tr>
                        {% endfor %}
                    </tr>
                </table>
        </center>
                <br />
                <a href="javascript:;" onclick=show()>
                    <button class="button">
                        Request for JSON
                    </button>
                    <br/>
                    <br/>
                </a>
                <div id="expand">
                    <pre>
                        {{raw_json}}
                    </pre>
                </div>
        <center>
             {% else %}
                <p>
                    You submitted an empty form.
                </p>
            {% endif %}
        </center>

    </body>
</html>
