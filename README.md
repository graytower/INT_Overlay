# INT_Overlay

This is a demo for VXLAN-based INT, an INT system to monitor overlay network.

## Include

The program includes five folders: p4src, json, packet, topo and experiment.

### p4src

The P4 file which defines the packet processing logic of the switches.

### json

The output of compiling int_vxlan.p4 in **p4src** folders.

### packet

The python files used to send, receive, decode and upload INT information to the database.

### topo

The python files to build the network topology and down flow table.

### experiment

Some scripts for drawing pictures of experimental results.

## Getting started

1.	Install dependences:

- [Mininet](http://mininet.org/download/)
- [BMv2](https://github.com/p4lang/behavioral-model)
- [p4c](https://github.com/p4lang/p4c)
- [mysql](https://www.mysql.com/)
- [python](https://www.python.org/)

2. Compile code:

```
sudo p4c-bm2-ss --p4v 16 -o json/int_vxlan.json p4src/int_vxlan.p4
```

This will produce `int_vxlan.json` file needed for BMv2.

3. Setting up test network:
	
```
sudo python topo/FattreeTopo.py --json int_vxlan.json
```
This will bring up mininet with the constructed fat-tree topology.

In other terminal set up forwarding rules:

```
sh topo/FattreeCommands.sh
```

Now you can use the standard mininet CLI in the first terminal.

4. Open xterm for hosts on mininet cli, for example:

```
xterm h1 h8
```

now in h8:

```
python receive.py 10.0.1.10-10.0.8.10
```

Now h8 is ready to receive a packet from h1, decode and upload the INT information to database which is set up in advance.

In h1: 

```
python send.py 10.0.8.10
```
Now h1 sends a packet to h8.
