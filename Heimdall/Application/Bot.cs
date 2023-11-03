using Discord;
using Discord.Net;
using Discord.WebSocket;
using Microsoft.Extensions.Configuration;
using Newtonsoft.Json;
using System;
using System.Threading.Tasks;


namespace Heimdall.Application
{
	class Bot
	{
		private readonly DiscordSocketClient client;
		private readonly IConfiguration config;
		private const ulong guildID = 0;

		public Bot()
		{
			client = new DiscordSocketClient();
			client.Log += Log;
			client.Ready += ClientReady;

			var _builder = new ConfigurationBuilder()
				.SetBasePath( AppContext.BaseDirectory )
				.AddJsonFile( path: "config.json" );
			config = _builder.Build();
		}


		public static Task Main( string[] args ) => new Bot().MainAsync();

		public async Task MainAsync()
		{
			await client.LoginAsync( TokenType.Bot, config[ "Token" ] );
			await client.StartAsync();
			await Task.Delay( -1 );
		}

		public async Task MainAsync( string[] args ) { }


		private Task Log( LogMessage log )
		{
			Console.WriteLine( log.ToString() );
			return Task.CompletedTask;
		}


		public async Task ClientReady()
		{
			var guild = client.GetGuild( guildID );
			var guildCommandPing = new SlashCommandBuilder()
				.WithName( "ping" )
				.WithDescription( "ping pong" );

			// Let's do our global command
			//var globalCommand = new SlashCommandBuilder();
			//globalCommand.WithName( "first-global-command" );
			//globalCommand.WithDescription( "This is my first global slash command" );

			client.SlashCommandExecuted += GuildSlashCommandPingHandler;

			try
			{
				await guild.CreateApplicationCommandAsync( guildCommandPing.Build() );
			}
			catch ( ApplicationCommandException exception )
			{
				var json = JsonConvert.SerializeObject( exception.Errors, Formatting.Indented );
				Console.WriteLine( json );
			}
		}


		private async Task GuildSlashCommandPingHandler( SocketSlashCommand command )
		{
			await command.RespondAsync( "pong" );
		}
	}
}


