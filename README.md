### We continue to develop our virtual assistant with a CLI interface.

Our assistant already knows how to interact with the user using the command line, receiving commands and arguments and performing the necessary actions. In this task, we will work on the internal logic of the assistant, how data is stored, what data it is, and what can be done with it.

We will use object-oriented programming for these purposes. First, let's select several entities (models) with which we will work.

The user will have an `address book` or a `contact book`. This `contact book` contains `records`. Each `record` contains some set of `fields`.

In this way, we have described the entities (classes) that need to be implemented. Next, we will consider the requirements for these classes and establish their relationship, the rules by which they will interact.

Essences:

`Field:` Base class for record fields. It will be the parent for all fields, it implements common logic for all fields

`Name:` A class for storing the name of a contact. Mandatory field.

`Phone:` A class for storing a phone number. Has format validation (10 digits). An optional field with a phone number, and one Record can contain several such fields.

`Record:` A class for storing information about a contact, including name and phone list. Responsible for the logic of adding/removing/editing optional fields and storing the mandatory field Name

`AddressBook:` A class for storing and managing records. Inherits from UserDict, and contains the logic of searching for entries in this class

---
