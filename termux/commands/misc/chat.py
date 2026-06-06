from stellar_translate import translate
from rich.console import Console
import asyncio
from rich.panel import Panel

console = Console()

async def receive_msg(reader, writer):
    try:
        addr = writer.get_extra_info('peername')
        ip_origen = addr[0] if addr else "Desconocida"
        data = await reader.read(1024)
        if data:
            mensaje = data.decode('utf-8')
            print("\n")
            msg = Panel(f"""
{mensaje}
            """, title=f"[bold white]From[/bold white] [bold red]{ip_origen}[/bold red]", border_style="bold cyan")
            
            console.print(msg, justify="right")
            
    except Exception as e:
        console.print(f"[bold red][ERROR][/bold red] {translate(category='user-config', type='error_message')} > {e}")
    finally:
        writer.close()
        await writer.wait_closed()

async def receive():
    try:
        server = await asyncio.start_server(receive_msg, '0.0.0.0', 5556, reuse_address=True)
        
        async with server:
            await server.serve_forever()
            
    except Exception as e:
        console.print(f"[bold red][ERROR][/bold red] {translate(category='user-config', type='error_message')} > {e}")
        return
        
async def send(destiny_ip, message):
    try:
        reader, writer = await asyncio.open_connection(destiny_ip, 5556)
        writer.write(f"{message}".encode('utf-8'))
        await writer.drain()
        writer.close()
        await writer.wait_closed()
        
    except Exception as e:
       console.print(f"[bold red][ERROR][/bold red] {translate(category='user-config', type='error_message')} > {e}")
       return
       

async def main():
    try:
        asyncio.create_task(receive())
        while True:
            message = await asyncio.to_thread(console.input, "[bold green]msg > [/bold green]")
            destiny_ip = await asyncio.to_thread(console.input, "[bold yellow]For: [/bold yellow]")
            
            if not message:
                console.print(f"[bold red][ERROR][/bold red] {translate(category='user-config', type='invalid_data_message')}")
                continue
            elif not destiny_ip:
                console.print(f"[bold red][ERROR][/bold red] {translate(category='user-config', type='invalid_data_message')}")
                continue                   
            else:
                await send(destiny_ip, message)
             
    except Exception as e:
        print("\n")
        console.print(f"[bold red][ERROR][/bold red] {translate(category='user-config', type='error_message')} > {e}")
        return
        

asyncio.run(main())