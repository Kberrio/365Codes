package main

import (
	"fmt"
	"log"
	"os"

	"github.com/go-resty/resty/v2"
)

const apiKey = "YOUR_RIOT_API_KEY"
const baseURL = "https://na1.api.riotgames.com/lol/static-data/v3"

type Champion struct {
	ID   int    `json:"id"`
	Name string `json:"name"`
	Title string `json:"title"`
}

func main() {
	if len(os.Args) < 2 {
		log.Fatalf("Usage: %s <champion_name>", os.Args[0])
	}
	championName := os.Args[1]

	client := resty.New()
	resp, err := client.R().
		SetQueryParams(map[string]string{
			"api_key": apiKey,
		}).
		SetResult(&Champion{}).
		Get(fmt.Sprintf("%s/champions?name=%s", baseURL, championName))

	if err != nil {
		log.Fatalf("Error fetching champion data: %v", err)
	}

	if resp.IsError() {
		log.Fatalf("Error response from API: %s", resp.Status())
	}

	champion := resp.Result().(*Champion)
	fmt.Printf("Champion ID: %d\n", champion.ID)
	fmt.Printf("Champion Name: %s\n", champion.Name)
	fmt.Printf("Champion Title: %s\n", champion.Title)
}
