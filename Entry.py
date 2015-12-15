from urlparse import urlparse

class Entry:
   'Model for memetracker entries (one per line)'
   numEntries = 0

   def __init__(self, lines): #lines should be a python list of lines in an entry
      self.quotes = []
      self.links = []
      self.url = ''
      self.timestamp = ''
      # get url
      for line in lines:
        if line.startswith('P'): # is url line (should be first line)
          self.url = line.split('\t')[1]
          lines.remove(line)
          break
      assert(self.url)

      # get timestamp
      for line in lines:
        if line.startswith('T'): # is the timestamp line (should be next line)
          self.timestamp = line.split('\t')[1]
          lines.remove(line)
          break
      assert(self.timestamp)

      # get quotes
      for line in lines:
        if line.startswith('Q'):
          self.quotes.append(line.split('\t')[1])

      # get links
      for line in lines:
        if line.startswith('L'):
          self.links.append(line.split('\t')[1])


      Entry.numEntries += 1
   
   def __str__(self):
    s = ''
    s += 'URL:'+self.url+'\n'
    s += 'TIME:'+ self.timestamp +'\n'
    if self.quotes:
      s += 'QUOTES:\n'
      for q in self.quotes:
        s += '\t'+q+'\n'
    else:
      s += 'NO QUOTES\n'
    if self.links:
      s += 'LINKS:\n'
      for l in self.links:
        s += '\t'+l+'\n'
    else:
      s += 'NO LINKS\n'

    return s

   def get_base_url(self): #not done
      parsed_uri = urlparse(self.url)
      domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
      return domain
