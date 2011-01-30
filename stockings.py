import random, copy

baggs = set(['Martin', 'Sharon', 'Sarah', 'David', 'Becca', 'Hannah', 'Grandpa'])
john_beseda = set(['John', 'Helen', 'Addie', 'Anna'])
jim_beseda = set(['Jim', 'Lori', 'Maggie', 'Joe'])

everybody = baggs | john_beseda | jim_beseda
getters = copy.copy(everybody)

condition = True
while condition:
    try:
        for person in everybody:
          if person in baggs:
            persons_getter = john_beseda | jim_beseda
          elif person in john_beseda:
            persons_getter = jim_beseda | baggs
          elif person in jim_beseda:
            persons_getter = john_beseda | baggs

          candidates = (persons_getter & getters) - set(person)
          candidate = random.choice(list(candidates))
          getters.remove(candidate)
          print person + ' -> ' + candidate
          condition = False
    except:
        continue

