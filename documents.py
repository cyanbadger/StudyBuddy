documents = [
    {
        "id": "doc_001",
        "topic": "Normalization in DBMS",
        "text": """
Normalization is the process of organizing data in a database to reduce redundancy and improve data integrity.
The main normal forms are 1NF, 2NF, 3NF, and BCNF. First Normal Form removes repeating groups and ensures
atomic values. Second Normal Form removes partial dependency on a composite key. Third Normal Form removes
transitive dependency. BCNF is a stronger version of 3NF where every determinant must be a candidate key.
Normalization helps avoid update anomalies, insertion anomalies, and deletion anomalies.
""".strip()
    },
    {
        "id": "doc_002",
        "topic": "ER Model",
        "text": """
The Entity Relationship model is used in database design to represent entities, attributes, and relationships.
An entity is a real-world object such as Student or Course. Attributes describe properties of entities, such as
student_id or name. Relationships show how entities are connected, such as a Student enrolls in a Course.
ER diagrams are widely used for conceptual database design before converting the design into relational tables.
""".strip()
    },
    {
        "id": "doc_003",
        "topic": "CNN",
        "text": """
Convolutional Neural Networks are deep learning models mainly used for image processing tasks. They use
convolution layers to extract features, pooling layers to reduce spatial dimensions, and fully connected layers
for final classification. CNNs are effective because they automatically learn hierarchical spatial features such
as edges, textures, and shapes from input images.
""".strip()
    },
    {
        "id": "doc_004",
        "topic": "LSTM",
        "text": """
LSTM stands for Long Short-Term Memory and is a special type of recurrent neural network designed to learn long-term
dependencies. It uses gates such as the forget gate, input gate, and output gate to control information flow.
LSTMs are useful in sequence tasks such as language modeling, speech recognition, and time-series prediction.
They solve the vanishing gradient problem better than basic RNNs.
""".strip()
    },
    {
        "id": "doc_005",
        "topic": "Hill Climbing",
        "text": """
Hill climbing is a local search algorithm used in artificial intelligence. It starts from an initial state and
moves to a neighboring state with a better evaluation value. The process continues until no better neighbor is found.
It is simple and efficient but can get stuck in local maxima, plateaus, and ridges. Variants include simple hill
climbing, steepest-ascent hill climbing, and stochastic hill climbing.
""".strip()
    },
    {
        "id": "doc_006",
        "topic": "Hidden Markov Model",
        "text": """
A Hidden Markov Model is a probabilistic model used for sequence data where the system is assumed to be a Markov process
with hidden states. It consists of states, transition probabilities, emission probabilities, and initial probabilities.
HMMs are used in speech recognition, part-of-speech tagging, and bioinformatics. The hidden state sequence is inferred
from the observed outputs.
""".strip()
    },
    {
        "id": "doc_007",
        "topic": "TCP vs UDP",
        "text": """
TCP is a connection-oriented transport protocol that provides reliable communication through acknowledgments,
sequencing, retransmission, and flow control. UDP is a connectionless transport protocol that provides faster but
unreliable communication without guaranteed delivery. TCP is used in web browsing, email, and file transfer.
UDP is commonly used in streaming, gaming, and DNS.
""".strip()
    },
    {
        "id": "doc_008",
        "topic": "OSI Model",
        "text": """
The OSI model is a seven-layer conceptual framework for understanding network communication. The seven layers are
Physical, Data Link, Network, Transport, Session, Presentation, and Application. Each layer performs a specific
function and communicates with the layer above and below it. The OSI model helps in network design, troubleshooting,
and understanding protocol behavior.
""".strip()
    },
    {
        "id": "doc_009",
        "topic": "ID3 Algorithm",
        "text": """
ID3 is a decision tree learning algorithm that uses entropy and information gain to select the best attribute for
splitting the dataset. Entropy measures impurity, while information gain measures the reduction in entropy after a split.
The attribute with the highest information gain is chosen at each step. ID3 works well for categorical data but can
overfit if the tree becomes too deep.
""".strip()
    },
    {
        "id": "doc_010",
        "topic": "K-Means Clustering",
        "text": """
K-means is an unsupervised machine learning algorithm used to partition data into k clusters. It works by initializing
k centroids, assigning each point to the nearest centroid, recomputing centroids, and repeating until convergence.
The goal is to minimize the within-cluster sum of squares. K-means is simple and fast but sensitive to initialization
and the value of k.
""".strip()
    }
]