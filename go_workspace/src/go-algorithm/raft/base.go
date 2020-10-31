package raft

import (
	"bufio"
	"os"
	"strconv"
)

type LogEntry struct {
	Command string
	Index   int
	Term    int
}

type server struct {
	dataDir string
	// Persistant, non-volatile state
	currentTerm int
	votedFor    int
	log         []LogEntry
	// volatile state
	CommitIndex int
	LastApplied int
}

type leader struct {
	server
	// reinitialize after election
	NextIndex  []int
	MatchIndex []int
}

func NewServer(dataDir string) *server {
	f, err := os.Open(dataDir + "term.txt")
	if err != nil {
		panic(err)
	}

	reader := bufio.NewReader(f)
	lines := make([]string, 0)
	var line string
	for {
		line, err = reader.ReadString('\n')
		if err != nil {
			break
		}
		lines = append(lines, line)
	}
	f.Close()
	currentTerm := 0
	if len(lines) != 0 {
		currentTerm, err = strconv.Atoi(lines[len(lines)-1])
		if err != nil {
			panic(err)
		}
	}
	// bufio.NewReadWriter{}
	return &server{dataDir: dataDir, currentTerm: currentTerm, votedFor: -1}
}

func (server *server) GetCurrentTerm() int {
	return 0
}
func (server *server) PersistCurrentTerm(t int) {

}
func (server *server) GetVotedFor() int {
	return 0
}

func (server *server) PersistVotedFor(v int) {

}
