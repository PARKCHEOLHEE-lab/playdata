function empall() {
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            data = this.responseText;
            data = JSON.parse(data);



            tab =
                `<table border="1"><tr><th>EMPNO</th><th>ENAME</th><th>SAL</th></tr>`;

            let empno;
            let ename;
            let sal;

            for (no in data) {
                empno = data[no].empno;
                ename = data[no].ename
                sal = data[no].sal

                tab = tab + `<tr>
                        <td>${empno}</td>
                        <td>${ename}</td>
                        <td>${sal}</td>
                    </tr>`;
            }

            tab = tab + `</table>`;
            document.getElementById("table").innerHTML = tab;

        }

    };

    xhttp.open("GET", "empall");
    xhttp.send();
}
