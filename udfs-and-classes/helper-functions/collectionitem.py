


# collectionitem class that takes in a dictionary
class Collectionitem:
  collectionitemcnt = 0
# stores a dictionary in self.colldict at the instantiation
  def __init__(self, colldict):
    self.colldict = colldict
    Collectionitem.collectionitemcnt+=1
# gets the birthyear of the first creator
  def birthyearcreator1(self):
    if ("birth_year" in self.colldict['creators'][0]):
      byear = self.colldict['creators'][0]['birth_year']
    else:
      byear = "Unknown"
    return byear
# gets the birthyear of each creator while also accounting for nulls with the get function
  def birthyearsall(self):
    byearlist = [item.get('birth_year') for item in self.colldict['creators']] # get to account for null values
    return byearlist
# returns number of creators
  def ncreators(self):
    return len(self.colldict['creators'])
# returns number of citations
  def ncitations(self):
    return len(self.colldict['citations'])
