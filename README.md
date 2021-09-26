# Fast direct access to compressed memory

## Paper-based comparison
https://hardworkar.notion.site/RAM-Compression-7b3e8925086b4e64ae7c036f00b1c7c9

## Existing stuff

#### software
- zswap
- zram
- Hurricane (Helix Software Company)
- quantization?
- Active Memory Expansion
- 842 compression algorithm on POWER7+ chip
- Wilson-Kaplan WKdm algorithm (Apple)

#### hardware
- IBM MXT - dedicated processor for transfers local cache <-> RAM

### Shortcomings???

- Low compression ratios - check this out

- Background I/O

- Increased thrashing - not understandable from wiki
