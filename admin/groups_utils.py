from github import Github # pip install PyGithub


def load_repos(print_groups=False):
    # load personal access token
    with open(r"C:\Users\hms467\OneDrive - University of Copenhagen\Documents\Arbejde\Undervisning\IPNA_2024\Github\token.txt", mode = "r") as file:
        token = file.read()

    year = "2024"    
    class_name = "projects-" + year


    # a. access github through access token.
    gh = Github(token)
    org = gh.get_organization('NumEconCopenhagen')
    all_repos = org.get_repos()

    # b. locate all repositories in current class
    disregard_repos = ['lucas-og-anna']

    current_class = [repo.name for repo in all_repos if (class_name in repo.name) & (repo.name not in disregard_repos)]

    if print_groups:
        # see this years' repos
        for r in current_class:
            print(r.removeprefix(class_name+"-"))

    return class_name, all_repos, current_class, disregard_repos