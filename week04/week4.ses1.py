#def extract_nft_names(nft_collection):
    
# time and space complexity: O(n) for both time and space, where n is the number of NFTs in the collection.
def extract_nft_names(nft_collection):
    nft_names = []
    # Iterating through the list once, taking O(n) time
    for nft in nft_collection:
        #Appending takes constant time
        nft_names.append(nft["name"])
    return nft_names

# Example usage:
nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))


def identify_popular_creators(nft_collection):
    creator_count = {}
    
    # Counting the occurrences of each creator
    for nft in nft_collection:
        creator = nft["creator"]
        if creator in creator_count:
            creator_count[creator] += 1
        else:
            creator_count[creator] = 1
    
    # Finding the maximum count
    max_count = max(creator_count.values())
    
    # Collecting creators with the maximum count
    popular_creators = [creator for creator, count in creator_count.items() if count == max_count and count > 1]
    
    return popular_creators

#output
# ['ArtByAlex']
# ['SpaceArt']
# []



nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(identify_popular_creators(nft_collection))
print(identify_popular_creators(nft_collection_2))
print(identify_popular_creators(nft_collection_3))



def average_nft_value(nft_collection):
    total = 0
    if len(nft_collection) == 0:
        return 0
    for value in nft_collection:
        total += value["value"]
    return total/len(nft_collection)

#output
# 5.7
# 9.15
# 0

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]
print(average_nft_value(nft_collection))

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
    {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}
]
print(average_nft_value(nft_collection_2))

nft_collection_3 = []
print(average_nft_value(nft_collection_3))


def search_nft_by_tag(nft_collections, tag):
    results=[]
    for collection in nft_collections:
        for nft in collection:
            if tag in nft["tags"]:
                results.append(nft["name"])
    return results            

#output
# ['Urban Jungle', 'City Lights']
# ['Golden Hour', 'Sunset Serenade']
# []

nft_collections = [
    [
        {"name": "Abstract Horizon", "tags": ["abstract", "modern"]},
        {"name": "Pixel Dreams", "tags": ["pixel", "retro"]}
    ],
    [
        {"name": "Urban Jungle", "tags": ["urban", "landscape"]},
        {"name": "City Lights", "tags": ["modern", "landscape"]}
    ]
]

nft_collections_2 = [
    [
        {"name": "Golden Hour", "tags": ["sunset", "landscape"]},
        {"name": "Sunset Serenade", "tags": ["sunset", "serene"]}
    ],
    [
        {"name": "Pixel Odyssey", "tags": ["pixel", "adventure"]}
    ]
]

nft_collections_3 = [
    [
        {"name": "The Last Piece", "tags": ["finale", "abstract"]}
    ],
    [
        {"name": "Ocean Waves", "tags": ["seascape", "calm"]},
        {"name": "Mountain Peak", "tags": ["landscape", "adventure"]}
    ]
]

print(search_nft_by_tag(nft_collections, "landscape"))
print(search_nft_by_tag(nft_collections_2, "sunset"))
print(search_nft_by_tag(nft_collections_3, "modern"))




def process_nft_queue(nft_queue):
    result=[]
    for nft in nft_queue:
        # Simulating processing time
        result.append(nft["name"])
    return result
#output
# ['Abstract Horizon', 'Pixel Dreams', 'Urban Jungle']
# ['Golden Hour', 'Sunset Serenade', 'Ocean Waves']
# ['Crypto Kitty', 'Galactic Voyage']

nft_queue = [
    {"name": "Abstract Horizon", "processing_time": 2},
    {"name": "Pixel Dreams", "processing_time": 3},
    {"name": "Urban Jungle", "processing_time": 1}
]
print(process_nft_queue(nft_queue))

nft_queue_2 = [
    {"name": "Golden Hour", "processing_time": 4},
    {"name": "Sunset Serenade", "processing_time": 2},
    {"name": "Ocean Waves", "processing_time": 3}
]
print(process_nft_queue(nft_queue_2))

nft_queue_3 = [
    {"name": "Crypto Kitty", "processing_time": 5},
    {"name": "Galactic Voyage", "processing_time": 6}
]
print(process_nft_queue(nft_queue_3))    



def validate_nft_actions(actions):
    keepCount = 0
    for action in actions:
        if action == "add":
            keepCount += 1 #0
        elif action == "remove":
            keepCount -= 1
        if keepCount < 0:
            return False
    return keepCount == 0

#output
# True
# True
# False

actions = ["add", "add", "remove", "remove"]
actions_2 = ["add", "remove", "add", "remove"]
actions_3 = ["add", "remove", "remove", "add"]

print(validate_nft_actions(actions))
print(validate_nft_actions(actions_2))
print(validate_nft_actions(actions_3))

# def find_closest_nft_values(nft_values, budget):
    
# nft_values = [3.5, 5.4, 7.2, 9.0, 10.5]
# nft_values_2 = [2.0, 4.5, 6.3, 7.8, 12.1]
# nft_values_3 = [1.0, 2.5, 4.0, 6.0, 9.0]

# print(find_closest_nft_values(nft_values, 8.0))
# print(find_closest_nft_values(nft_values_2, 6.5))
# print(find_closest_nft_values(nft_values_3, 3.0))