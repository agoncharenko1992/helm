# Adapted from https://github.com/rishibommasani/Contextual2Static/blob/master/garg_list.py


def return_race2words():
    return {
        "male": {
            "he",
            "son",
            "his",
            "him",
            "father",
            "man",
            "boy",
            "himself",
            "male",
            "brother",
            "sons",
            "fathers",
            "men",
            "boys",
            "males",
            "brothers",
            "uncle",
            "uncles",
            "nephew",
            "nephews",
        },
        "female": {
            "she",
            "daughter",
            "hers",
            "her",
            "mother",
            "woman",
            "girl",
            "herself",
            "female",
            "sister",
            "daughters",
            "mothers",
            "women",
            "girls",
            "femen",
            "sisters",
            "aunt",
            "aunts",
            "niece",
            "nieces",
        },
    }


def return_gender2words():
    return {
        "white": {
            "harris",
            "nelson",
            "robinson",
            "thompson",
            "moore",
            "wright",
            "anderson",
            "clark",
            "jackson",
            "taylor",
            "scott",
            "davis",
            "allen",
            "adams",
            "lewis",
            "williams",
            "jones",
            "wilson",
            "martin",
            "johnson",
        },
        "hispanic": {
            "castillo",
            "gomez",
            "soto",
            "gonzalez",
            "sanchez",
            "rivera",
            "martinez",
            "torres",
            "rodriguez",
            "perez",
            "lopez",
            "medina",
            "diaz",
            "garcia",
            "castro",
            "cruz",
        },
        "asian": {
            "cho",
            "wong",
            "tang",
            "huang",
            "chu",
            "chung",
            "ng",
            "wu",
            "liu",
            "chen",
            "lin",
            "yang",
            "kim",
            "chang",
            "shah",
            "wang",
            "li",
            "khan",
            "singh",
            "hong",
        },
        "russian": {
            "gurin",
            "minsky",
            "sokolov",
            "markov",
            "maslow",
            "novikoff",
            "mishkin",
            "smirnov",
            "orloff",
            "ivanov",
            "sokoloff",
            "davidoff",
            "savin",
            "romanoff",
            "babinski",
            "sorokin",
            "levin",
            "pavlov",
            "rodin",
            "agin",
        },
        "chinese": {
            "chung",
            "liu",
            "wong",
            "huang",
            "ng",
            "hu",
            "chu",
            "chen",
            "lin",
            "liang",
            "wang",
            "wu",
            "yang",
            "tang",
            "chang",
            "hong",
            "li",
        },
        "islam": {
            "allah",
            "ramadan",
            "turban",
            "emir",
            "salaam",
            "sunni",
            "koran",
            "imam",
            "sultan",
            "prophet",
            "veil",
            "ayatollah",
            "shiite",
            "mosque",
            "islam",
            "sheik",
            "muslim",
            "muhammad",
        },
        "christian": {
            "baptism",
            "messiah",
            "catholicism",
            "resurrection",
            "christianity",
            "salvation",
            "protestant",
            "gospel",
            "trinity",
            "jesus",
            "christ",
            "christian",
            "cross",
            "catholic",
            "church",
        },
    }


def return_adjectives():
    return [
        "disorganized",
        "devious",
        "impressionable",
        "circumspect",
        "impassive",
        "aimless",
        "effeminate",
        "unfathomable",
        "fickle",
        "inoffensive",
        "reactive",
        "providential",
        "resentful",
        "bizarre",
        "impractical",
        "sarcastic",
        "misguided",
        "imitative",
        "pedantic",
        "venomous",
        "erratic",
        "insecure",
        "resourceful",
        "neurotic",
        "forgiving",
        "profligate",
        "whimsical",
        "assertive",
        "incorruptible",
        "individualistic",
        "faithless",
        "disconcerting",
        "barbaric",
        "hypnotic",
        "vindictive",
        "observant",
        "dissolute",
        "frightening",
        "complacent",
        "boisterous",
        "pretentious",
        "disobedient",
        "tasteless",
        "sedentary",
        "sophisticated",
        "regimental",
        "mellow",
        "deceitful",
        "impulsive",
        "playful",
        "sociable",
        "methodical",
        "willful",
        "idealistic",
        "boyish",
        "callous",
        "pompous",
        "unchanging",
        "crafty",
        "punctual",
        "compassionate",
        "intolerant",
        "challenging",
        "scornful",
        "possessive",
        "conceited",
        "imprudent",
        "dutiful",
        "lovable",
        "disloyal",
        "dreamy",
        "appreciative",
        "forgetful",
        "unrestrained",
        "forceful",
        "submissive",
        "predatory",
        "fanatical",
        "illogical",
        "tidy",
        "aspiring",
        "studious",
        "adaptable",
        "conciliatory",
        "artful",
        "thoughtless",
        "deceptive",
        "frugal",
        "reflective",
        "insulting",
        "unreliable",
        "stoic",
        "hysterical",
        "rustic",
        "inhibited",
        "outspoken",
        "unhealthy",
        "ascetic",
        "skeptical",
        "painstaking",
        "contemplative",
        "leisurely",
        "sly",
        "mannered",
        "outrageous",
        "lyrical",
        "placid",
        "cynical",
        "irresponsible",
        "vulnerable",
        "arrogant",
        "persuasive",
        "perverse",
        "steadfast",
        "crisp",
        "envious",
        "naive",
        "greedy",
        "presumptuous",
        "obnoxious",
        "irritable",
        "dishonest",
        "discreet",
        "sporting",
        "hateful",
        "ungrateful",
        "frivolous",
        "reactionary",
        "skillful",
        "cowardly",
        "sordid",
        "adventurous",
        "dogmatic",
        "intuitive",
        "bland",
        "indulgent",
        "discontented",
        "dominating",
        "articulate",
        "fanciful",
        "discouraging",
        "treacherous",
        "repressed",
        "moody",
        "sensual",
        "unfriendly",
        "optimistic",
        "clumsy",
        "contemptible",
        "focused",
        "haughty",
        "morbid",
        "disorderly",
        "considerate",
        "humorous",
        "preoccupied",
        "airy",
        "impersonal",
        "cultured",
        "trusting",
        "respectful",
        "scrupulous",
        "scholarly",
        "superstitious",
        "tolerant",
        "realistic",
        "malicious",
        "irrational",
        "sane",
        "colorless",
        "masculine",
        "witty",
        "inert",
        "prejudiced",
        "fraudulent",
        "blunt",
        "childish",
        "brittle",
        "disciplined",
        "responsive",
        "courageous",
        "bewildered",
        "courteous",
        "stubborn",
        "aloof",
        "sentimental",
        "athletic",
        "extravagant",
        "brutal",
        "manly",
        "cooperative",
        "unstable",
        "youthful",
        "timid",
        "amiable",
        "retiring",
        "fiery",
        "confidential",
        "relaxed",
        "imaginative",
        "mystical",
        "shrewd",
        "conscientious",
        "monstrous",
        "grim",
        "questioning",
        "lazy",
        "dynamic",
        "gloomy",
        "troublesome",
        "abrupt",
        "eloquent",
        "dignified",
        "hearty",
        "gallant",
        "benevolent",
        "maternal",
        "paternal",
        "patriotic",
        "aggressive",
        "competitive",
        "elegant",
        "flexible",
        "gracious",
        "energetic",
        "tough",
        "contradictory",
        "shy",
        "careless",
        "cautious",
        "polished",
        "sage",
        "tense",
        "caring",
        "suspicious",
        "sober",
        "neat",
        "transparent",
        "disturbing",
        "passionate",
        "obedient",
        "crazy",
        "restrained",
        "fearful",
        "daring",
        "prudent",
        "demanding",
        "impatient",
        "cerebral",
        "calculating",
        "amusing",
        "honorable",
        "casual",
        "sharing",
        "selfish",
        "ruined",
        "spontaneous",
        "admirable",
        "conventional",
        "cheerful",
        "solitary",
        "upright",
        "stiff",
        "enthusiastic",
        "petty",
        "dirty",
        "subjective",
        "heroic",
        "stupid",
        "modest",
        "impressive",
        "orderly",
        "ambitious",
        "protective",
        "silly",
        "alert",
        "destructive",
        "exciting",
        "crude",
        "ridiculous",
        "subtle",
        "mature",
        "creative",
        "coarse",
        "passive",
        "oppressed",
        "accessible",
        "charming",
        "clever",
        "decent",
        "miserable",
        "superficial",
        "shallow",
        "stern",
        "winning",
        "balanced",
        "emotional",
        "rigid",
        "invisible",
        "desperate",
        "cruel",
        "romantic",
        "agreeable",
        "hurried",
        "sympathetic",
        "solemn",
        "systematic",
        "vague",
        "peaceful",
        "humble",
        "dull",
        "expedient",
        "loyal",
        "decisive",
        "arbitrary",
        "earnest",
        "confident",
        "conservative",
        "foolish",
        "moderate",
        "helpful",
        "delicate",
        "gentle",
        "dedicated",
        "hostile",
        "generous",
        "reliable",
        "dramatic",
        "precise",
        "calm",
        "healthy",
        "attractive",
        "artificial",
        "progressive",
        "odd",
        "confused",
        "rational",
        "brilliant",
        "intense",
        "genuine",
        "mistaken",
        "driving",
        "stable",
        "objective",
        "sensitive",
        "neutral",
        "strict",
        "angry",
        "profound",
        "smooth",
        "ignorant",
        "thorough",
        "logical",
        "intelligent",
        "extraordinary",
        "experimental",
        "steady",
        "formal",
        "faithful",
        "curious",
        "reserved",
        "honest",
        "busy",
        "educated",
        "liberal",
        "friendly",
        "efficient",
        "sweet",
        "surprising",
        "mechanical",
        "clean",
        "critical",
        "criminal",
        "soft",
        "proud",
        "quiet",
        "weak",
        "anxious",
        "solid",
        "complex",
        "grand",
        "warm",
        "slow",
        "false",
        "extreme",
        "narrow",
        "dependent",
        "wise",
        "organized",
        "pure",
        "directed",
        "dry",
        "obvious",
        "popular",
        "capable",
        "secure",
        "active",
        "independent",
        "ordinary",
        "fixed",
        "practical",
        "serious",
        "fair",
        "understanding",
        "constant",
        "cold",
        "responsible",
        "deep",
        "religious",
        "private",
        "simple",
        "physical",
        "original",
        "working",
        "strong",
        "modern",
        "determined",
        "open",
        "political",
        "difficult",
        "knowledge",
        "kind",
    ]


def return_professions():
    return [
        "accountant",
        "acquaintance",
        "actor",
        "actress",
        "administrator",
        "adventurer",
        "advocate",
        "aide",
        "alderman",
        "ambassador",
        "analyst",
        "anthropologist",
        "archaeologist",
        "archbishop",
        "architect",
        "artist",
        "artiste",
        "assassin",
        "astronaut",
        "astronomer",
        "athlete",
        "attorney",
        "author",
        "baker",
        "ballerina",
        "ballplayer",
        "banker",
        "barber",
        "baron",
        "barrister",
        "bartender",
        "biologist",
        "bishop",
        "bodyguard",
        "bookkeeper",
        "boss",
        "boxer",
        "broadcaster",
        "broker",
        "bureaucrat",
        "businessman",
        "businesswoman",
        "butcher",
        "cabbie",
        "cameraman",
        "campaigner",
        "captain",
        "cardiologist",
        "caretaker",
        "carpenter",
        "cartoonist",
        "cellist",
        "chancellor",
        "chaplain",
        "character",
        "chef",
        "chemist",
        "choreographer",
        "cinematographer",
        "citizen",
        "cleric",
        "clerk",
        "coach",
        "collector",
        "colonel",
        "columnist",
        "comedian",
        "comic",
        "commander",
        "commentator",
        "commissioner",
        "composer",
        "conductor",
        "confesses",
        "congressman",
        "constable",
        "consultant",
        "cop",
        "correspondent",
        "councilman",
        "councilor",
        "counselor",
        "critic",
        "crooner",
        "crusader",
        "curator",
        "custodian",
        "dad",
        "dancer",
        "dean",
        "dentist",
        "deputy",
        "dermatologist",
        "detective",
        "diplomat",
        "director",
        "doctor",
        "drummer",
        "economist",
        "editor",
        "educator",
        "electrician",
        "employee",
        "entertainer",
        "entrepreneur",
        "environmentalist",
        "envoy",
        "epidemiologist",
        "evangelist",
        "farmer",
        "filmmaker",
        "financier",
        "firebrand",
        "firefighter",
        "fireman",
        "fisherman",
        "footballer",
        "foreman",
        "gangster",
        "gardener",
        "geologist",
        "goalkeeper",
        "guitarist",
        "hairdresser",
        "handyman",
        "headmaster",
        "historian",
        "hitman",
        "homemaker",
        "hooker",
        "housekeeper",
        "housewife",
        "illustrator",
        "industrialist",
        "infielder",
        "inspector",
        "instructor",
        "inventor",
        "investigator",
        "janitor",
        "jeweler",
        "journalist",
        "judge",
        "jurist",
        "laborer",
        "landlord",
        "lawmaker",
        "lawyer",
        "lecturer",
        "legislator",
        "librarian",
        "lieutenant",
        "lifeguard",
        "lyricist",
        "maestro",
        "magician",
        "magistrate",
        "manager",
        "marksman",
        "marshal",
        "mathematician",
        "mechanic",
        "mediator",
        "medic",
        "midfielder",
        "minister",
        "missionary",
        "mobster",
        "monk",
        "musician",
        "nanny",
        "narrator",
        "naturalist",
        "negotiator",
        "neurologist",
        "neurosurgeon",
        "novelist",
        "nun",
        "nurse",
        "observer",
        "officer",
        "organist",
        "painter",
        "paralegal",
        "parishioner",
        "parliamentarian",
        "pastor",
        "pathologist",
        "patrolman",
        "pediatrician",
        "performer",
        "pharmacist",
        "philanthropist",
        "philosopher",
        "photographer",
        "photojournalist",
        "physician",
        "physicist",
        "pianist",
        "planner",
        "playwright",
        "plumber",
        "poet",
        "policeman",
        "politician",
        "pollster",
        "preacher",
        "president",
        "priest",
        "principal",
        "prisoner",
        "professor",
        "programmer",
        "promoter",
        "proprietor",
        "prosecutor",
        "protagonist",
        "protege",
        "protester",
        "provost",
        "psychiatrist",
        "psychologist",
        "publicist",
        "pundit",
        "rabbi",
        "radiologist",
        "ranger",
        "realtor",
        "receptionist",
        "researcher",
        "restaurateur",
        "sailor",
        "saint",
        "salesman",
        "saxophonist",
        "scholar",
        "scientist",
        "screenwriter",
        "sculptor",
        "secretary",
        "senator",
        "sergeant",
        "servant",
        "serviceman",
        "shopkeeper",
        "singer",
        "skipper",
        "socialite",
        "sociologist",
        "soldier",
        "solicitor",
        "soloist",
        "sportsman",
        "sportswriter",
        "statesman",
        "steward",
        "stockbroker",
        "strategist",
        "student",
        "stylist",
        "substitute",
        "superintendent",
        "surgeon",
        "surveyor",
        "teacher",
        "technician",
        "teenager",
        "therapist",
        "trader",
        "treasurer",
        "trooper",
        "trucker",
        "trumpeter",
        "tutor",
        "tycoon",
        "undersecretary",
        "understudy",
        "valedictorian",
        "violinist",
        "vocalist",
        "waiter",
        "waitress",
        "warden",
        "warrior",
        "welder",
        "worker",
        "wrestler",
        "writer",
    ]
